#!/usr/bin/env python3
"""Render a DOCX to PDF and page PNGs with an isolated LibreOffice profile."""
import argparse
from pathlib import Path
from scripts.office_renderer import render

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("input", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True); parser.add_argument("--emit-pdf", action="store_true")
    parser.add_argument("--dpi", type=int, default=144); args = parser.parse_args()
    render(args.input, args.output_dir, args.emit_pdf, args.dpi)

if __name__ == "__main__": main()
