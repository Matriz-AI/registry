#!/usr/bin/env python3
"""Remove notes or review comments from a PPTX package on explicit request."""
import argparse, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

REL = "{http://schemas.openxmlformats.org/package/2006/relationships}"
CT = "{http://schemas.openxmlformats.org/package/2006/content-types}"

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("input", type=Path); parser.add_argument("output", type=Path)
    parser.add_argument("--notes", action="store_true"); parser.add_argument("--comments", action="store_true"); args = parser.parse_args()
    if not (args.notes or args.comments): raise SystemExit("Choose --notes and/or --comments.")
    with zipfile.ZipFile(args.input) as source: entries = {i.filename: source.read(i.filename) for i in source.infolist()}
    prefixes = (["ppt/notesSlides/", "ppt/notesMasters/"] if args.notes else []) + (["ppt/comments/", "ppt/commentAuthors.xml"] if args.comments else [])
    entries = {n: d for n, d in entries.items() if not any(n.startswith(prefix) for prefix in prefixes)}
    for name, data in list(entries.items()):
        if name.endswith(".rels"):
            root = ET.fromstring(data)
            for rel in list(root):
                target = rel.attrib.get("Target", "")
                if (args.notes and "notes" in target.lower()) or (args.comments and "comment" in target.lower()): root.remove(rel)
            entries[name] = ET.tostring(root, encoding="utf-8", xml_declaration=True)
        elif name == "[Content_Types].xml":
            root = ET.fromstring(data)
            for item in list(root):
                part = item.attrib.get("PartName", "").lower()
                if (args.notes and "notes" in part) or (args.comments and "comment" in part): root.remove(item)
            entries[name] = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    with zipfile.ZipFile(args.output, "w", zipfile.ZIP_DEFLATED) as output:
        for name, data in entries.items(): output.writestr(name, data)

if __name__ == "__main__": main()
