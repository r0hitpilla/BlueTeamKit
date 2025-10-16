#!/usr/bin/env python3
import json, time
MITRE_MAP = {
    "ransom_note_created": {"tech":"T1486","desc":"Data Encrypted for Impact - ransom note"},
    "locked_files": {"tech":"T1486","desc":"Files locked/renamed"},
    "high_write_rate": {"tech":"T1486","desc":"High file write activity"}
}
def build_html(timeline_file="timeline.json", out="timeline.html"):
    with open(timeline_file) as f:
        events = json.load(f)
    html = "<html><body><h1>RansomSim Timeline</h1><ul>"
    for e in events:
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(e.get("time",0)))
        ev = e.get("event")
        m = MITRE_MAP.get(ev, {})
        html += f\"<li><b>{t}</b> - {ev} - {m.get('tech','N/A')} - {m.get('desc','')} - details: {e}</li>\"
    html += "</ul></body></html>"
    with open(out,"w") as f:
        f.write(html)
    print("[+] Timeline HTML written to", out)

if __name__=="__main__":
    build_html()
