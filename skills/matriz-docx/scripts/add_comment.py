#!/usr/bin/env python3
"""Add a Word review comment to the first run containing a requested phrase."""
import argparse
from pathlib import Path
from docx import Document

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path); parser.add_argument("output", type=Path)
    parser.add_argument("--find", required=True); parser.add_argument("--text", required=True)
    parser.add_argument("--author", default="Matriz AI"); parser.add_argument("--initials", default="MA")
    args = parser.parse_args(); document = Document(args.input)
    for paragraph in document.paragraphs:
        for run in paragraph.runs:
            if args.find in run.text:
                document.add_comment(run, text=args.text, author=args.author, initials=args.initials)
                document.save(args.output); return
    raise SystemExit(f"Text not found: {args.find!r}")

if __name__ == "__main__": main()
