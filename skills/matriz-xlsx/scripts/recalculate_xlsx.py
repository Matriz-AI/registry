#!/usr/bin/env python3
"""Recalculate an XLSX through LibreOffice, or request recalc on next open."""
import argparse, os, shutil, subprocess, tempfile
from pathlib import Path
from openpyxl import load_workbook

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("input", type=Path); parser.add_argument("output", type=Path); args = parser.parse_args()
    soffice = os.environ.get("SOFFICE_PATH") or shutil.which("soffice") or shutil.which("libreoffice")
    if soffice:
        with tempfile.TemporaryDirectory(prefix="matriz-lo-") as profile, tempfile.TemporaryDirectory(prefix="matriz-xlsx-") as out:
            subprocess.run([soffice, f"-env:UserInstallation={Path(profile).as_uri()}", "--headless", "--convert-to", "xlsx", "--outdir", out, str(args.input)], check=True)
            generated = Path(out) / args.input.name
            if generated.exists(): shutil.copy2(generated, args.output); return
    book = load_workbook(args.input); book.calculation.fullCalcOnLoad = True; book.calculation.forceFullCalc = True; book.save(args.output)
    print("LibreOffice unavailable; workbook marked for recalculation on next open.")

if __name__ == "__main__": main()
