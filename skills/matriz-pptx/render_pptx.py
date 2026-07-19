#!/usr/bin/env python3
"""Render a PPTX to PDF and slide PNGs using isolated LibreOffice state."""
import argparse, os, shutil, subprocess, tempfile
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("input", type=Path); parser.add_argument("--output-dir", type=Path, required=True); parser.add_argument("--emit-pdf", action="store_true"); parser.add_argument("--dpi", type=int, default=144); args = parser.parse_args()
    soffice = os.environ.get("SOFFICE_PATH") or shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice: raise SystemExit("LibreOffice not found. Set SOFFICE_PATH to soffice executable.")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="matriz-lo-") as profile:
        subprocess.run([soffice, f"-env:UserInstallation={Path(profile).as_uri()}", "--headless", "--convert-to", "pdf", "--outdir", str(args.output_dir), str(args.input)], check=True)
    pdf = args.output_dir / f"{args.input.stem}.pdf"; converter = shutil.which("pdftoppm")
    if not pdf.exists() or not converter: raise SystemExit("PDF or pdftoppm unavailable; cannot create slide images.")
    subprocess.run([converter, "-png", "-r", str(args.dpi), str(pdf), str(args.output_dir / "slide")], check=True)
    if not args.emit_pdf: pdf.unlink()

if __name__ == "__main__": main()
