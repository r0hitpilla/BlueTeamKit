#!/usr/bin/env python3
import json, subprocess, sys, os

INVENTORY_FILE = "assets/discovered.json"

def run_nmap(host):
    # basic port/service discovery
    cmd = ["nmap", "-sV", "-oX", "-", host]
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
        return out.decode('utf-8')
    except Exception as e:
        print("Nmap error:", e)
        return ""

def discovery_from_list(input_file="assets/sample_inventory.json"):
    with open(input_file) as f:
        assets = json.load(f)
    results = []
    for a in assets:
        host = a.get("host") or a.get("name")
        print(f"[+] Scanning {host}")
        xml = run_nmap(host)
        # For simplicity, store host and raw xml result
        results.append({"asset": host, "nmap_xml": xml})
    os.makedirs(os.path.dirname(INVENTORY_FILE), exist_ok=True)
    with open(INVENTORY_FILE, "w") as f:
        json.dump(results, f, indent=2)
    print("[+] Discovery written to", INVENTORY_FILE)

if __name__ == "__main__":
    discovery_from_list()
