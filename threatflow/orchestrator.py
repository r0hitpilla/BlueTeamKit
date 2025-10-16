#!/usr/bin/env python3
import os, subprocess

steps = [
    "python3 asset_discovery.py",
    "python3 vuln_scanner.py",
    "python3 risk_scoring.py",
    "python3 patch_tracker.py"
]

def run_all():
    cwd = os.path.dirname(__file__)
    for s in steps:
        print("[*] Running:", s)
        subprocess.call(s, shell=True, cwd=cwd)

if __name__=="__main__":
    run_all()
