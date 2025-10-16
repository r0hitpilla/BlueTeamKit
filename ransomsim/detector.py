#!/usr/bin/env python3
"""
Simple detector that monitors sample_data/ for:
 - sudden increase in file writes (by checking modification times)
 - files renamed with .locked extension
 - presence of RECOVER_YOUR_FILES.txt
Logs findings to timeline.json
"""
import os, time, json
DATA_DIR = "sample_data"
TIMELINE = "timeline.json"

def snapshot():
    state = {}
    for f in os.listdir(DATA_DIR):
        p = os.path.join(DATA_DIR,f)
        try:
            state[f] = os.path.getmtime(p)
        except:
            state[f] = 0
    return state

def monitor(duration=30, interval=1):
    timeline = []
    prev = snapshot()
    for _ in range(int(duration/interval)):
        time.sleep(interval)
        curr = snapshot()
        # detect new ransom note
        if "RECOVER_YOUR_FILES.txt" in curr and "RECOVER_YOUR_FILES.txt" not in prev:
            timeline.append({"time": time.time(), "event":"ransom_note_created"})
            print("[!] ransom note created")
        # detect .locked files
        locked = [f for f in curr if f.endswith(".locked")]
        if locked:
            timeline.append({"time": time.time(), "event":"locked_files", "files": locked})
            print("[!] locked files detected:", locked)
        # detect many file modifies
        changed = [f for f in curr if prev.get(f,0) != curr[f]]
        if len(changed) > 10:
            timeline.append({"time": time.time(), "event":"high_write_rate", "count": len(changed)})
            print("[!] high write rate:", len(changed))
        prev = curr
    with open(TIMELINE,"w") as f:
        json.dump(timeline,f,indent=2)
    print("[+] Timeline written to", TIMELINE)

if __name__=="__main__":
    monitor(30,1)
