# 🛡️ Cyber Threat Intelligence (CTI) Integration 

<div align="center">

# 🔍 Cyber Threat Intelligence Integration & Risk Analysis

### Collect • Process • Analyze • Prioritize • Visualize Threat Intelligence

![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python)
![Threat Intelligence](https://img.shields.io/badge/Threat_Intelligence-CTI-red?style=for-the-badge)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Analysis-blue?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-Data_Processing-black?style=for-the-badge&logo=json)
![CSV](https://img.shields.io/badge/CSV-Data_Analysis-green?style=for-the-badge)
![LibreOffice](https://img.shields.io/badge/LibreOffice-Calc-18A303?style=for-the-badge&logo=libreoffice)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-orange?style=for-the-badge)

</div>

---

# 📖 Overview

Cyber Threat Intelligence (CTI) enables organizations to understand adversaries, identify emerging threats, and make informed security decisions.

In this hands-on lab, students will learn how to:

- 🕵️ Collect threat intelligence from open-source feeds
- 📊 Process and normalize CTI datasets
- 🎯 Prioritize threats using risk scoring methodologies
- 👤 Identify human-targeted security threats
- 📈 Visualize threat landscapes
- 📝 Generate actionable security recommendations

This lab simulates real-world CTI workflows used by Security Operations Centers (SOCs), Threat Intelligence Teams, and Incident Response Analysts.

---

# 🎯 Objectives

By the end of this lab, students will be able to:

✅ Integrate open-source CTI data into structured formats

✅ Analyze and prioritize threats using intelligence indicators

✅ Build risk assessment frameworks using Python

✅ Identify human-driven security threats

✅ Generate actionable security recommendations

---

# 📚 Prerequisites

Before beginning this lab, students should have:

- 🛡️ Basic cybersecurity knowledge
- 🐧 Linux command-line familiarity
- 🐍 Basic Python programming skills
- 📄 Understanding of CSV and JSON formats
- 📊 Fundamental security analysis concepts

---

# ☁️ Lab Environment

Al Nafi provides pre-configured Linux cloud machines.

### Included Tools

- Ubuntu Linux
- Python 3
- pip3
- LibreOffice Calc
- curl
- JSON Utilities

Verify Environment:

```bash
python3 --version
pip3 --version
libreoffice --version
```

Expected Output:

```text
Python 3.x
pip 23.x
LibreOffice 7.x+
```

---

# 📁 Project Structure

Create workspace:

```bash
mkdir -p ~/cti_lab/{data,scripts,output}
cd ~/cti_lab
```

Expected Structure:

```text
cti_lab/
├── data/
├── scripts/
└── output/
```

---

# 🛠️ Task 1 — Collect and Process CTI Data

---

## 🔹 Step 1.1 Download Open Source Threat Intelligence

Download threat feeds:

```bash
# Malware indicators
curl -o data/malware_hashes.csv "https://bazaar.abuse.ch/export/csv/recent/"

# Malicious IP addresses
curl -o data/feodo_ips.csv "https://feodotracker.abuse.ch/downloads/ipblocklist.csv"

# Malicious URLs and domains
curl -o data/urlhaus_domains.csv "https://urlhaus.abuse.ch/downloads/csv/"
```

Backup original files:

```bash
cp -r data data_backup
```

Verify downloads:

```bash
ls -lh data/
```

Expected Output:

```text
malware_hashes.csv
feodo_ips.csv
urlhaus_domains.csv
```

---

## 🔹 Step 1.2 Create CTI Data Processing Script

Create script:

```bash
nano scripts/process_cti.py
```

Insert the provided starter code from the lab instructions.

---

### Processing Functions

The script should:

✔ Process MalwareBazaar indicators

✔ Process Feodo Tracker IPs

✔ Process URLhaus domains

✔ Normalize records

✔ Export JSON and CSV datasets

---

Run Script:

```bash
python3 scripts/process_cti.py
```

Expected Output:

```text
Processed 150 indicators
```

Generated Files:

```text
output/master_cti_dataset.json
output/master_cti_dataset.csv
```

---

## 🔹 Step 1.3 Create CTI Spreadsheet

Create spreadsheet generator:

```bash
nano scripts/create_spreadsheet.py
```

Insert the provided starter code.

---

### Risk Scoring Logic

| Factor | Score |
|----------|---------|
| High Threat | 7 |
| Medium Threat | 4 |
| Low Threat | 1 |
| Trusted Source | +2 |
| URL/Domain | +3 |
| IP Address | +2 |
| File Hash | +1 |

Maximum Score:

```text
10
```

---

Run Spreadsheet Generator

```bash
python3 scripts/create_spreadsheet.py
```

Open Results:

```bash
libreoffice --calc output/cti_main_sheet.csv &
```

Generated Files:

```text
cti_main_sheet.csv
cti_risk_summary.csv
```

---

# 📊 Task 2 — Analyze and Prioritize Threats

---

## 🔹 Step 2.1 Create Risk Analysis Framework

Create analyzer:

```bash
nano scripts/risk_analyzer.py
```

Insert provided class template.

---

### Analysis Components

The analyzer performs:

- Threat Landscape Analysis
- Priority Score Calculation
- Human Risk Analysis
- Recommendation Generation
- Report Creation

---

### Priority Score Model

| Score | Action |
|---------|------------|
| 12-15 | Immediate Response |
| 8-11 | Urgent Investigation |
| 5-7 | Scheduled Review |
| 1-4 | Monitor |

---

## 🔹 Step 2.2 Execute Risk Analysis

Run analyzer:

```bash
python3 scripts/risk_analyzer.py
```

Expected Output:

```text
Threat analysis completed
Risk report generated
```

Generated Report:

```text
output/risk_assessment_report.json
```

---

## 🔹 Step 2.3 Create Risk Prioritization Matrix

Create matrix generator:

```bash
nano scripts/risk_matrix.py
```

Insert starter code.

Run:

```bash
python3 scripts/risk_matrix.py
```

Open Results:

```bash
libreoffice --calc output/risk_matrix.csv &
```

---

### Risk Matrix

| Category | Score |
|-----------|---------|
| Critical | 12-15 |
| High | 8-11 |
| Medium | 5-7 |
| Low | 1-4 |

---

# 📈 Task 3 — Visualize Threat Intelligence

---

## 🔹 Step 3.1 Create Threat Visualization Dashboard

Create dashboard:

```bash
nano scripts/visualize_threats.py
```

Insert starter code.

---

### Dashboard Visualizations

📊 Threat Level Distribution

📈 Indicator Type Breakdown

📉 Priority Score Histogram

📋 Top Threat Sources

---

Run Dashboard Generator

```bash
python3 scripts/visualize_threats.py
```

Open Dashboard:

```bash
firefox output/threat_dashboard.html &
```

Generated File:

```text
output/threat_dashboard.html
```

---

# 👤 Human Risk Analysis

One of the primary goals of CTI is identifying threats that exploit human behavior.

Examples include:

### Phishing

```text
Malicious URLs
Fake Login Pages
Credential Harvesting
```

### Social Engineering

```text
Business Email Compromise
Fake Support Calls
Identity Spoofing
```

### Malware Delivery

```text
Malicious Attachments
Trojan Installers
User-Initiated Execution
```

Risk Scoring Factors:

| Human Risk Indicator | Score Bonus |
|---------------------|-------------|
| URL/Domain | +3 |
| Social Engineering Keywords | +2 |
| User-Targeting Malware | +2 |

---

# 📋 Verification Checklist

Run these commands:

```bash
echo "=== Verify CTI Data ==="
ls output/

echo "=== Verify JSON Dataset ==="
python3 -m json.tool output/master_cti_dataset.json | head

echo "=== Verify Risk Matrix ==="
cat output/risk_matrix.csv

echo "=== Verify Dashboard ==="
ls -lh output/threat_dashboard.html
```

---

# 📊 Expected Outcomes

After completing this lab, students will have:

✅ 150+ CTI Indicators Processed

✅ Master Threat Intelligence Dataset

✅ Risk Prioritization Framework

✅ Human Risk Assessment Capability

✅ Threat Visualization Dashboard

✅ Security Recommendation Engine

---

# 📂 Generated Files

| File | Description |
|--------|---------------|
| master_cti_dataset.json | Combined CTI dataset |
| master_cti_dataset.csv | Normalized indicators |
| cti_main_sheet.csv | Main spreadsheet |
| cti_risk_summary.csv | Risk summary |
| risk_assessment_report.json | Threat analysis |
| risk_matrix.csv | Threat prioritization |
| threat_dashboard.html | Threat dashboard |

---

# 🚨 Troubleshooting

---

## Download Fails with SSL Error

```bash
curl --insecure -o data/file.csv "URL"
```

---

## CSV Parsing Errors

Check file contents:

```bash
head -20 data/file.csv
```

Check encoding:

```bash
file -i data/file.csv
```

---

## Empty Data

Verify downloads:

```bash
ls -lh data/
```

Check contents:

```bash
head data/malware_hashes.csv
```

---

## LibreOffice Issues

Kill existing processes:

```bash
killall soffice.bin
```

Restart:

```bash
libreoffice --calc output/cti_main_sheet.csv &
```

---

## JSON Errors

Validate file:

```bash
python3 -m json.tool output/master_cti_dataset.json
```

---

# 🎓 Key Skills Learned

Through this lab, students gained practical experience in:

🔹 Cyber Threat Intelligence Collection

🔹 Threat Data Normalization

🔹 Security Risk Scoring

🔹 Threat Prioritization

🔹 Human Risk Analysis

🔹 Threat Visualization

🔹 Security Recommendation Development

🔹 Threat Intelligence Reporting

---

# 🔗 Additional Resources

### Threat Intelligence Platforms

- MISP Threat Sharing Platform
- OpenCTI
- ThreatConnect

### Frameworks

- MITRE ATT&CK
- STIX/TAXII
- Diamond Model

### Intelligence Sources

- MalwareBazaar
- Feodo Tracker
- URLhaus

---

# 🏆 Conclusion

This lab demonstrated how Cyber Threat Intelligence can be transformed from raw threat indicators into actionable security insights.

Students successfully:

✔ Collected threat intelligence from open sources

✔ Processed and normalized CTI datasets

✔ Calculated risk and priority scores

✔ Identified human-focused cyber threats

✔ Generated risk matrices and recommendations

✔ Created security dashboards for decision-making

The techniques learned in this lab mirror the workflows used by modern SOC teams, Threat Intelligence Analysts, Blue Teams, and Incident Response professionals.

By combining CTI with risk analysis and human-focused threat assessment, organizations can make smarter security decisions, improve resource allocation, and proactively defend against emerging cyber threats.

---

<div align="center">

# 🎯 Lab Completed Successfully

### Cyber Threat Intelligence (CTI) Integration & Risk Assessment

⭐ Ready for Advanced Threat Hunting & Threat Intelligence Operations

</div>
