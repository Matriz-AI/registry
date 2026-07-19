#!/usr/bin/env python3
"""Render a DOCX to PDF and page PNGs with an isolated LibreOffice profile."""
import argparse, os, shutil, subprocess, tempfile
from pathlib import Path

def executable():
    return os.environ.get("SOFFICE_PATH") or shutil.which("soffice") or shutil.which("libreoffice")

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("input", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True); parser.add_argument("--emit-pdf", action="store_true")
    parser.add_argument("--dpi", type=int, default=144); args = parser.parse_args(); soffice = executable()
    if not soffice: raise SystemExit("LibreOffice not found. Set SOFFICE_PATH to soffice executable.")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="matriz-lo-") as profile:
        command = [soffice, f"-env:UserInstallation={Path(profile).as_uri()}", "--headless", "--convert-to", "pdf", "--outdir", str(args.output_dir), str(args.input)]
        subprocess.run(command, check=True, capture_output=True, text=True)
    pdf = args.output_dir / (args.input.stem + ".pdf")
    if not pdf.exists(): raise SystemExit("LibreOffice did not create a PDF.")
    converter = shutil.which("pdftoppm")
    if not converter: raise SystemExit("pdftoppm not found; PDF created but page PNGs could not be generated.")
    subprocess.run([converter, "-png", "-r", str(args.dpi), str(pdf), str(args.output_dir / "page")], check=True)
    if not args.emit_pdf: pdf.unlink()

if __name__ == "__main__": main()
