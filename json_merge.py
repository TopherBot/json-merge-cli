#!/usr/bin/env python3
"""json_merge.py – Merge two JSON files.

Usage:
    python json_merge.py <file1.json> <file2.json> > merged.json

If a key exists in both files, the value from the second file prevails.
Nested dictionaries are merged recursively.
"""
import json
import sys
from pathlib import Path

def merge(a, b):
    """Recursively merge dict *b* into dict *a* and return the result.
    Non‑dict values from *b* overwrite those in *a*.
    """
    if not isinstance(a, dict) or not isinstance(b, dict):
        return b
    result = dict(a)  # shallow copy
    for key, b_val in b.items():
        a_val = result.get(key)
        result[key] = merge(a_val, b_val) if isinstance(b_val, dict) else b_val
    return result

def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: json_merge.py <file1.json> <file2.json>\n")
        sys.exit(1)
    file1, file2 = map(Path, sys.argv[1:])
    try:
        data1 = json.loads(file1.read_text())
        data2 = json.loads(file2.read_text())
    except Exception as e:
        sys.stderr.write(f"Error reading JSON: {e}\n")
        sys.exit(1)
    merged = merge(data1, data2)
    json.dump(merged, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write('\n')

if __name__ == "__main__":
    main()
