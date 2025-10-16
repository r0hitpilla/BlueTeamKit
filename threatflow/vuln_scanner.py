#!/usr/bin/env python3
import json, os, re
from xml.etree import ElementTree as ET

# tiny mock vuln DB keyed by product/version substrings
MOCK_VULN_DB = {
    "nginx 1.14": [{"cve":"CVE-2020-1234","desc":"Example NGINX vuln","cvss":7.5}],
    "mysql 8.0": [{"cve":"CVE-2021-5678","desc":"Example MySQL vuln","cvss":9.0}],
    "apache 2.4": [{"cve":"CVE-2019-0001","desc":"Example Apache vuln","cvss":6.5}]
}

DISCOVERED = "assets/discovered.json"
OUTPUT = "assets/vuln_report.json"

def scan_and_match():
    if not os.path.exists(DISCOVERED):
        print("Run asset discovery first.")
        return
    with open(DISCOVERED) as f:
        items = json.load(f)
    results = []
    for it in items:
        host = it.get("asset")
        xml = it.get("nmap_xml","")
        # parse xml for service product/version
        vulns = []
        try:
            root = ET.fromstring(xml)
            for port in root.findall(".//port"):
                service = port.find("service")
                if service is None: continue
                product = (service.get("product") or "").lower()
                version = (service.get("version") or "")
                key = None
                for k in MOCK_VULN_DB.keys():
                    if k in f\"{product} {version}\":
                        key = k
                        break
                if key:
                    vulns += MOCK_VULN_DB[key]
        except Exception:
            # fallback: simple text matching
            for k in MOCK_VULN_DB.keys():
                if k.split()[0] in xml.lower():
                    vulns += MOCK_VULN_DB[k]
        results.append({"asset": host, "vulns": vulns})
    with open(OUTPUT,"w") as f:
        json.dump(results,f,indent=2)
    print("[+] Vulnerability report written to", OUTPUT)

if __name__=="__main__":
    scan_and_match()
