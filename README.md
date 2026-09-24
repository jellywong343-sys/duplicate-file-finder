# Duplicate File Finder

[绠€浣撲腑鏂嘳(README.zh-CN.md)

Find duplicate files using file size grouping and SHA-256 checksums without deleting anything.

## Highlights

- Python standard library only; no runtime dependencies.
- Command-line interface and automated tests included.
- Safe defaults and clear output.
- Windows, macOS, and Linux; Python 3.10+.

## Installation

```bash
git clone https://github.com/jellywong343-sys/duplicate-file-finder.git
cd duplicate-file-finder
python -m pip install -e .
```

Replace `jellywong343-sys` with your GitHub username.

## Usage

```bash
find-duplicates ~/Downloads
find-duplicates ~/Downloads --min-size 1024 --json duplicates.json
```

Run `find-duplicates --help` to see every option.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
duplicate-file-finder/
鈹溾攢鈹€ src/duplicate_file_finder/
鈹溾攢鈹€ tests/
鈹溾攢鈹€ README.md
鈹溾攢鈹€ README.zh-CN.md
鈹溾攢鈹€ pyproject.toml
鈹斺攢鈹€ LICENSE
```

## Safety

Review command output before applying changes to important files. Keep backups of irreplaceable data.

## License

MIT



