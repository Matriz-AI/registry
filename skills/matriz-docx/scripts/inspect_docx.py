#!/usr/bin/env python3
"""Emit a compact structural report for a DOCX without changing it."""
import argparse, json, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

def count(root, tag): return len(root.findall(".//" + W + tag))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    with zipfile.ZipFile(args.input) as package:
        names = set(package.namelist())
        root = ET.fromstring(package.read("word/document.xml"))
        report = {
            "file": args.input.name, "paragraphs": count(root, "p"), "tables": count(root, "tbl"),
            "images": len([n for n in names if n.startswith("word/media/")]),
            "comments": "word/comments.xml" in names, "trackedInsertions": count(root, "ins"),
            "trackedDeletions": count(root, "del"), "headers": len([n for n in names if n.startswith("word/header")]),
            "footers": len([n for n in names if n.startswith("word/footer")]), "customProperties": "docProps/custom.xml" in names,
        }
    payload = json.dumps(report, indent=2) + "\n"
    if args.out: args.out.write_text(payload, encoding="utf-8")
    else: print(payload, end="")

if __name__ == "__main__": main()
