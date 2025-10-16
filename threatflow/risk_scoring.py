#!/usr/bin/env python3
import json

INFILE = "assets/vuln_report.json"
OUTFILE = "assets/vuln_report_scored.json"

def score():
    with open(INFILE) as f:
        data = json.load(f)
    for entry in data:
        for v in entry.get("vulns", []):
            cvss = v.get("cvss")
            try:
                score = float(cvss)
            except:
                score = 0.0
            if score >= 9:
                v['risk'] = "Critical"
            elif score >= 7:
                v['risk'] = "High"
            elif score >=4:
                v['risk'] = "Medium"
            else:
                v['risk'] = "Low"
    with open(OUTFILE, "w") as f:
        json.dump(data, f, indent=2)
    print("[+] Scored report written to", OUTFILE)

if __name__=="__main__":
    score()
