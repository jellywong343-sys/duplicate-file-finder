import sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/"src"))
from duplicate_file_finder.cli import find_duplicates
class Tests(unittest.TestCase):
 def test_duplicates(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp); (root/"a.txt").write_text("same"); (root/"b.txt").write_text("same"); (root/"c.txt").write_text("different")
   groups=find_duplicates(root); self.assertEqual(len(groups),1); self.assertEqual(len(groups[0]["files"]),2)
if __name__ == "__main__": unittest.main()
