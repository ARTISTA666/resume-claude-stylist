#!/usr/bin/env python3
"""
render_pdf.py - Headless Chrome PDF compiler with strict 1-page verification
Part of Antigravity skill: resume-claude-stylist
"""

import sys
import os
import argparse
import subprocess

def find_chrome():
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "google-chrome",
        "chromium",
        "chromium-browser"
    ]
    for c in candidates:
        if os.path.isfile(c) and os.access(c, os.X_OK):
            return c
        # check if in PATH
        which = subprocess.run(["which", c], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if which.returncode == 0 and which.stdout.strip():
            return which.stdout.strip()
    return None

def compile_pdf(html_path, pdf_path):
    chrome_bin = find_chrome()
    if not chrome_bin:
        print("[ERROR] Chrome or Chromium binary not found on system.", file=sys.stderr)
        sys.exit(1)
        
    abs_html = os.path.abspath(html_path)
    abs_pdf = os.path.abspath(pdf_path)
    
    cmd = [
        chrome_bin,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={abs_pdf}",
        f"file://{abs_html}"
    ]
    
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print(f"[ERROR] Chrome headless compilation failed:\n{res.stderr}", file=sys.stderr)
        sys.exit(res.returncode)
        
    print(f"[SUCCESS] Compiled PDF: {abs_pdf}")
    
    # Check page count
    try:
        info_res = subprocess.run(["pdfinfo", abs_pdf], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if info_res.returncode == 0:
            for line in info_res.stdout.splitlines():
                if "Pages:" in line:
                    pages = int(line.split(":")[1].strip())
                    if pages == 1:
                        print("[VERIFIED] Resume is strictly 1 single page. Excellent!")
                    else:
                        print(f"[WARNING] Resume produced {pages} pages! Expected exactly 1 page.", file=sys.stderr)
                        print("  Please adjust CSS font-size or margins to fit on a single page.", file=sys.stderr)
    except FileNotFoundError:
        pass

def main():
    parser = argparse.ArgumentParser(description="Compile HTML resume to vector PDF via Chrome Headless.")
    parser.add_argument("--html", required=True, help="Input HTML resume path")
    parser.add_argument("--output", required=True, help="Output PDF path")
    args = parser.parse_args()
    
    compile_pdf(args.html, args.output)

if __name__ == "__main__":
    main()
