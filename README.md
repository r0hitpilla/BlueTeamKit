# BlueTeamKit

BlueTeamKit is a set of mini Blue Team projects for defensive cybersecurity and detection engineering. Includes HomeSOC, ThreatFlow, and RansomSim examples.

## Features

- Centralized log collection and alerting (HomeSOC)
- Automated vulnerability management workflow (ThreatFlow)
- Ransomware behavior detection simulation (RansomSim)
- MITRE ATT&CK mapping dashboards
- Fully open-source and customizable

---

## Quickstart

### 1. Clone the repo (if not already)

git clone https://github.com/r0hitpilla/BlueTeamKit.git
cd BlueTeamKit

### 2. Install dependencies

If Python projects are included

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt

### 3. Run each mini-project

python -m src.vulneye --inventory assets/sample_inventory.json --output docs/vulnerability_report.html

**HomeSoc/ Threatflow/ RansomSim**
Follow individual project instructions in their folders. Typically:

# Start HomeSOC ELK stack (if included)
docker-compose up -d

# Run ThreatFlow scripts
python src/threatflow.py

# Run RansomSim detection scripts
python src/ransomsim.py

