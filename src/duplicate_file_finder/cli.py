from __future__ import annotations
import argparse,hashlib,json
from collections import defaultdict
from pathlib import Path

def sha256(path:Path,chunk_size=1024*1024):
 digest=hashlib.sha256()
 with path.open("rb") as handle:
  while chunk:=handle.read(chunk_size): digest.update(chunk)
 return digest.hexdigest()

def find_duplicates(root:Path,min_size=1):
 root=root.expanduser().resolve()
 if not root.is_dir(): raise ValueError(f"Not a directory: {root}")
 by_size=defaultdict(list)
 for path in root.rglob("*"):
  try:
   if path.is_file() and not path.is_symlink() and path.stat().st_size>=min_size: by_size[path.stat().st_size].append(path)
  except OSError: continue
 results=[]
 for size,paths in by_size.items():
  if len(paths)<2: continue
  by_hash=defaultdict(list)
  for path in paths:
   try: by_hash[sha256(path)].append(path)
   except OSError: continue
  for checksum,matches in by_hash.items():
   if len(matches)>1: results.append({"size":size,"sha256":checksum,"files":[str(p) for p in matches]})
 return sorted(results,key=lambda item:(-item["size"],item["files"][0]))

def main():
 parser=argparse.ArgumentParser(description="Find duplicate files without deleting anything."); parser.add_argument("directory")
 parser.add_argument("--min-size",type=int,default=1); parser.add_argument("--json",dest="json_path"); args=parser.parse_args()
 groups=find_duplicates(Path(args.directory),args.min_size)
 if not groups: print("No duplicate files found.")
 for number,group in enumerate(groups,1):
  print(f"\nGroup {number}: {group['size']} bytes")
  for path in group["files"]: print(f"  {path}")
 if args.json_path: Path(args.json_path).write_text(json.dumps(groups,indent=2),encoding="utf-8"); print(f"\nJSON report: {args.json_path}")
 print("\nNo files were deleted.")
if __name__ == "__main__": main()
