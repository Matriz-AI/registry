"""PDF/PNG rendering with LibreOffice first and local Microsoft Office fallback."""
import base64, os, shutil, subprocess, tempfile
from pathlib import Path

OFFICE = {"docx": ("Word.Application", 17), "pptx": ("PowerPoint.Application", 2), "xlsx": ("Excel.Application", 0)}
def _soffice():
    candidates=[os.environ.get("SOFFICE_PATH"),shutil.which("soffice"),shutil.which("libreoffice")]
    for base in (os.environ.get("ProgramFiles"),os.environ.get("ProgramFiles(x86)")):
        if base: candidates.append(str(Path(base)/"LibreOffice"/"program"/"soffice.exe"))
    return next((p for p in candidates if p and Path(p).is_file()),None)
def _quote(value): return "'"+str(value).replace("'","''")+"'"
def _office_pdf(source,pdf,extension):
    shell=shutil.which("powershell.exe") or shutil.which("powershell")
    if not shell: raise RuntimeError("Microsoft Office fallback requires Windows PowerShell.")
    app,kind=OFFICE[extension]; source,target=_quote(source),_quote(pdf)
    if extension=="docx": body=f"$doc=$app.Documents.Open({source},$false,$true); $doc.ExportAsFixedFormat({target},{kind}); $doc.Close($false)"
    elif extension=="pptx": body=f"$doc=$app.Presentations.Open({source},$true,$false,$false); $doc.SaveAs({target},32); $doc.Close()"
    else: body=f"$app.DisplayAlerts=$false; $doc=$app.Workbooks.Open({source},0,$true); $doc.ExportAsFixedFormat({kind},{target}); $doc.Close($false)"
    script="$ErrorActionPreference='Stop'; $app=$null; try { $app=New-Object -ComObject "+app+"; "+body+" } finally { if ($app) { $app.Quit() } }"
    result=subprocess.run([shell,"-NoProfile","-NonInteractive","-EncodedCommand",base64.b64encode(script.encode("utf-16le")).decode("ascii")],capture_output=True,text=True)
    if result.returncode: raise RuntimeError((result.stderr or result.stdout).strip() or "Microsoft Office COM export failed.")
def render(input_file,output_dir,emit_pdf,dpi):
    input_file,output_dir=Path(input_file),Path(output_dir); extension=input_file.suffix.lower().lstrip(".")
    if extension not in OFFICE: raise ValueError(f"Unsupported format: {input_file.suffix}")
    output_dir.mkdir(parents=True,exist_ok=True); pdf=output_dir/f"{input_file.stem}.pdf"; failures=[]; soffice=_soffice()
    if soffice:
        try:
            with tempfile.TemporaryDirectory(prefix="matriz-lo-") as profile: subprocess.run([soffice,f"-env:UserInstallation={Path(profile).as_uri()}","--headless","--convert-to","pdf","--outdir",str(output_dir),str(input_file)],check=True,capture_output=True,text=True)
            if pdf.exists(): return _pages(pdf,output_dir,emit_pdf,dpi)
            failures.append("LibreOffice completed without producing a PDF")
        except Exception as error: failures.append(f"LibreOffice: {error}")
    try:
        _office_pdf(input_file,pdf,extension)
        if pdf.exists(): return _pages(pdf,output_dir,emit_pdf,dpi)
        failures.append("Microsoft Office completed without producing a PDF")
    except Exception as error: failures.append(f"Microsoft Office: {error}")
    raise RuntimeError("No Office rendering engine is available. Install LibreOffice or desktop Microsoft Office with its application registered for COM automation. "+("; ".join(failures) or "LibreOffice and Microsoft Office were not detected"))
def _pages(pdf,output_dir,emit_pdf,dpi):
    converter=shutil.which("pdftoppm")
    if converter:
        try: subprocess.run([converter,"-png","-r",str(dpi),str(pdf),str(output_dir/"slide")],check=True)
        except subprocess.CalledProcessError: converter=None
    if not converter:
        magick=shutil.which("magick")
        if not magick: raise RuntimeError("PDF created, but neither pdftoppm nor ImageMagick is available for PNG generation.")
        subprocess.run([magick,"-density",str(dpi),str(pdf),str(output_dir/"slide-%03d.png")],check=True)
    if not emit_pdf: pdf.unlink()
