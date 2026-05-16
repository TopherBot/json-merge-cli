# json-merge-cli

A minimal Python CLI tool for merging two JSON files.

## Usage
```bash
python json_merge.py <file1.json> <file2.json> > merged.json
```
- `file1.json` – base JSON object.
- `file2.json` – overrides/extends the base.
- The result is printed to stdout.

## How it works
The script loads both files, recursively merges dictionaries, and lets values from the second file replace those from the first when keys clash.

## Requirements
- Python 3.8+

## License
MIT – see the `LICENSE` file.
