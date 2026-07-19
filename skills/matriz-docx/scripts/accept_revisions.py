#!/usr/bin/env python3
"""Create a clean DOCX by accepting tracked insertions and deletions."""
import argparse, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
ET.register_namespace("w", W[1:-1])

def accept(node):
    for child in list(node):
        if child.tag == W + "del": node.remove(child); continue
        if child.tag == W + "ins":
            index = list(node).index(child)
            node.remove(child)
            for nested in list(child): node.insert(index, nested); index += 1
            continue
        accept(child)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path); parser.add_argument("output", type=Path)
    args = parser.parse_args()
    with zipfile.ZipFile(args.input) as source:
        entries = {item.filename: source.read(item.filename) for item in source.infolist()}
    for name in [n for n in entries if n.startswith("word/") and n.endswith(".xml")]:
        try:
            root = ET.fromstring(entries[name]); accept(root)
            entries[name] = ET.tostring(root, encoding="utf-8", xml_declaration=True)
        except ET.ParseError: pass
    with zipfile.ZipFile(args.output, "w", zipfile.ZIP_DEFLATED) as output:
        for name, data in entries.items(): output.writestr(name, data)

if __name__ == "__main__": main()
