#!/usr/bin/env python3
import csv, json, os
VULN_FILE = "assets/vuln_report_scored.json"
PATCH_CSV = "assets/patch_tracker.csv"

def init_csv():
    with open(PATCH_CSV, "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["asset","cve","cvss","risk","remediation_status","target_date","reboot_required"])
    print("[+] Patch tracker initialized:", PATCH_CSV)

def populate():
    if not os.path.exists(VULN_FILE):
        print("Run scoring first.")
        return
    with open(VULN_FILE) as f:
        data = json.load(f)
    rows = []
    for e in data:
        for v in e.get("vulns",[]):
            rows.append([e["asset"], v["cve"], v.get("cvss", "N/A"), v.get("risk","N/A"), "Pending", "2025-11-01", "Yes"])
    with open(PATCH_CSV,"a", newline='') as f:
        w = csv.writer(f)
        w.writerows(rows)
    print("[+] Patch tracker populated")

if __name__=="__main__":
    if not os.path.exists(PATCH_CSV):
        init_csv()
    populate()
