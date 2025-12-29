#!/usr/bin/env python3
"""Compare two key/value files and print keys whose values differ.

Format handling:
- Lines starting with or containing '!' are treated as comments (text after '!' ignored).
- Key/value separators supported: '=', ':', or whitespace (first whitespace splits key/value).
"""
from __future__ import annotations
import argparse
import sys
from typing import Dict


def parse_file(path: str) -> Dict[str, str]:
    d: Dict[str, str] = {}
    with open(path, encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            # strip comments that start with '!'
            line = line.split('!', 1)[0].strip()
            if not line:
                continue
            # split key/value by =, :, or first whitespace
            if '=' in line:
                key, val = line.split('=', 1)
            elif ':' in line:
                key, val = line.split(':', 1)
            else:
                parts = line.split(None, 1)
                if len(parts) == 1:
                    key, val = parts[0], ''
                else:
                    key, val = parts
            key = key.strip()
            val = val.strip()
            # strip surrounding quotes from value
            if (len(val) >= 2) and ((val[0] == val[-1]) and val[0] in ('"', "'")):
                val = val[1:-1]
            d[key] = val
    return d


def compare(file1: str, file2: str):
    a = parse_file(file1)
    b = parse_file(file2)
    all_keys = sorted(set(a.keys()) | set(b.keys()))
    print("| Key | File 1 Value | File 2 Value |")
    print("| --- | ------------ | ------------ |")
    for k in all_keys:
        val1 = a.get(k, "*")
        val2 = b.get(k, "*")
        if val1 != val2:
            print(f"| {k} | {val1} | {val2} |")


def main(argv=None):
    p = argparse.ArgumentParser(description="Print keys present in both files with differing values.")
    p.add_argument('file1', help='first input file')
    p.add_argument('file2', help='second input file')
    p.add_argument('-o', '--out', help='write output to file (defaults to stdout)')
    args = p.parse_args(argv)

    if args.out:
        with open(args.out, 'w', encoding='utf-8') as out:
            old = sys.stdout
            sys.stdout = out
            try:
                compare(args.file1, args.file2)
            finally:
                sys.stdout = old
    else:
        compare(args.file1, args.file2)


if __name__ == '__main__':
    main()

