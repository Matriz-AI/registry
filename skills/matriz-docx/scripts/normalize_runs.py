#!/usr/bin/env python3
"""Coalesce adjacent DOCX text runs with identical formatting."""
import argparse, copy, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
ET.register_namespace("w", W[1:-1])

def key(run):
    props = run.find(W + "rPr")
    return ET.tostring(props, encoding="unicode") if props is not None else ""

def merge(paragraph):
    runs = list(paragraph)
    previous = None
    for run in runs:
        if run.tag != W + "r" or previous is None or key(run) != key(previous):
            previous = run if run.tag == W + "r" else None
            continue
        previous_text = previous.find(W + "t")
        current_text = run.find(W + "t")
        if previous_text is None or current_text is None or len(run) != (2 if run.find(W + "rPr") is not None else 1):
            previous = run
            continue
        previous_text.text = (previous_text.text or "") + (current_text.text or "")
        paragraph.remove(run)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path); parser.add_argument("output", type=Path)
    args = parser.parse_args()
    with zipfile.ZipFile(args.input) as source:
        entries = {item.filename: source.read(item.filename) for item in source.infolist()}
    root = ET.fromstring(entries["word/document.xml"])
    for paragraph in root.findall(".//" + W + "p"): merge(paragraph)
    entries["word/document.xml"] = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    with zipfile.ZipFile(args.output, "w", zipfile.ZIP_DEFLATED) as output:
        for name, data in entries.items(): output.writestr(name, data)

if __name__ == "__main__": main()
