#!/usr/bin/env python3
"""
Safe Ransomware Simulator (no real encryption).
Creates many file writes, renames, and ransom-note files in sample_data/.
"""
import os, time, argparse, random

DATA_DIR = "sample_data"
def make_test_files(n=50):
    os.makedirs(DATA_DIR, exist_ok=True)
    for i in range(n):
        fn = os.path.join(DATA_DIR, f"file_{i}.txt")
        with open(fn,"w") as f:
            f.write("This is safe test content\\n")
    print(f"[+] Created {n} test files")

def simulate_activity(iterations=20, pause=0.2):
    files = [os.path.join(DATA_DIR,f) for f in os.listdir(DATA_DIR)]
    for it in range(iterations):
        # simulate rapid writes/overwrites
        target = random.choice(files)
        with open(target,"a") as f:
            f.write(f"append {it}\\n")
        # simulate rename (like ransomware preparing)
        if random.random() < 0.2:
            orig = target
            new = orig + ".locked"  # mark as 'locked' but not actually encrypted
            os.rename(orig, new)
            # revert occasionally to avoid permanent loss
            if random.random() < 0.5:
                os.rename(new, orig)
        # create ransom note file occasionally
        if random.random() < 0.1:
            rn = os.path.join(DATA_DIR,"RECOVER_YOUR_FILES.txt")
            with open(rn,"w") as f:
                f.write("Your files are encrypted. Contact attacker@example.com\\n")
        time.sleep(pause)

if __name__=="__main__":
    make_test_files(100)
    simulate_activity(100, 0.05)
