# 🛡️ Role-Based Risk Identification 

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Security](https://img.shields.io/badge/Cybersecurity-Risk%20Analysis-red)
![Status](https://img.shields.io/badge/Lab-Hands%20On-success)
![Focus](https://img.shields.io/badge/CTI-Threat%20Intelligence-orange)

---

## 📌 Overview

This lab focuses on **Role-Based Risk Identification**, a key concept in organizational cybersecurity risk management.  
Students will build a Python-based tool to analyze security risks associated with different organizational roles using:

- 🧠 Role attributes (access level, privilege, sensitivity)
- 🌐 Cyber Threat Intelligence (CTI)
- 📊 Risk scoring models
- 📈 Visualization & reporting

---

## 🎯 Objectives

By the end of this lab, you will be able to:

- 🏢 Understand role-based risk assessment in organizations
- 🔐 Identify security risks per job role
- 🐍 Develop Python-based risk analysis tools
- 🧾 Integrate CTI data into risk scoring
- 📊 Generate structured risk reports and visualizations
- 🚦 Classify roles into risk levels (CRITICAL → MINIMAL)

---

## ⚙️ Prerequisites

- 🐍 Basic Python programming
- 📂 Understanding of JSON files
- 🐧 Linux command line familiarity
- 🛡️ Basic organizational security concepts

---

## 🧪 Lab Environment

💻 This lab runs on **Al Nafi Cloud Linux Machines**

👉 Click **Start Lab** to access:
- Python 3 environment
- Pre-installed dependencies
- Ready-to-use workspace

---

## 📁 Project Structure

```text
role_risk_lab/
│
├── organizational_roles.json
├── cti_data.json
├── role_risk_analyzer.py
├── run_analysis.py
├── advanced_classifier.py
├── detailed_risk_report.txt
├── risk_report.json
└── visualization_charts.png
```

---

## 🚀 Task 1: Environment Setup

### 🔹 Create Project Directory

```bash
mkdir ~/role_risk_lab
cd ~/role_risk_lab
```

### 🔹 Create Virtual Environment

```bash
python3 -m venv risk_env
source risk_env/bin/activate
```

### 🔹 Install Dependencies

```bash
pip install pandas numpy matplotlib
```

---

## 📂 Task 2: Data Preparation

### 🧾 Organizational Roles (JSON)

Create the configuration file:

```bash
nano organizational_roles.json
```

Add the following role attributes (CEO 👔, IT Administrator 💻, HR Manager 👥, Sales Representative 📞, Support Agent 🎧):

```json
{
  "roles": [
    {
      "title": "CEO",
      "department": "Executive",
      "access_level": 9,
      "data_sensitivity": 10,
      "external_exposure": 8,
      "privilege_level": 9
    },
    {
      "title": "IT Administrator",
      "department": "IT",
      "access_level": 10,
      "data_sensitivity": 8,
      "external_exposure": 3,
      "privilege_level": 10
    },
    {
      "title": "HR Manager",
      "department": "HR",
      "access_level": 6,
      "data_sensitivity": 9,
      "external_exposure": 5,
      "privilege_level": 6
    },
    {
      "title": "Sales Representative",
      "department": "Sales",
      "access_level": 4,
      "data_sensitivity": 5,
      "external_exposure": 9,
      "privilege_level": 3
    },
    {
      "title": "Support Agent",
      "department": "Support",
      "access_level": 5,
      "data_sensitivity": 6,
      "external_exposure": 7,
      "privilege_level": 4
    }
  ]
}
```

### 🌐 CTI Threat Data

Create the CTI file (Phishing Attacks 🎯, Social Engineering 🧠, Insider Threats 🕵️):

```bash
nano cti_data.json
```

Add the targeted intelligence data:

```json
{
  "threats": [
    {
      "threat_type": "Phishing Attacks",
      "targeted_roles": ["CEO", "Sales Representative", "Support Agent"],
      "severity_modifier": 1.5
    },
    {
      "threat_type": "Social Engineering",
      "targeted_roles": ["CEO", "HR Manager"],
      "severity_modifier": 1.3
    },
    {
      "threat_type": "Insider Threats",
      "targeted_roles": ["IT Administrator"],
      "severity_modifier": 1.4
    }
  ]
}
```

---

## 🧠 Task 3: Role Risk Analyzer

### 🐍 File: role_risk_analyzer.py

Create the core processing engine:

```bash
nano role_risk_analyzer.py
```

Paste the following logic implementation:

```python
import json
import math

class RoleRiskAnalyzer:
    def __init__(self, roles_path, cti_path):
        self.roles_path = roles_path
        self.cti_path = cti_path
        self.roles_data = []
        self.cti_data = []

    def load_data(self):
        with open(self.roles_path, 'r') as f:
            self.roles_data = json.load(f).get('roles', [])
        with open(self.cti_path, 'r') as f:
            self.cti_data = json.load(f).get('threats', [])

    def calculate_base_score(self, role):
        # Formula: Risk = (Access × 0.3 + Sensitivity × 0.25 + Exposure × 0.25 + Privilege × 0.2) × 10
        score = (
            role['access_level'] * 0.3 +
            role['data_sensitivity'] * 0.25 +
            role['external_exposure'] * 0.25 +
            role['privilege_level'] * 0.2
        ) * 10
        return round(score, 2)

    def apply_cti_modifiers(self, role_title, base_score):
        modifier = 1.0
        for threat in self.cti_data:
            if role_title in threat['targeted_roles']:
                modifier += (threat['severity_modifier'] - 1.0)
        return round(base_score * modifier, 2)

    def classify_risk_level(self, score):
        if score >= 90: return "CRITICAL"
        elif score >= 70: return "HIGH"
        elif score >= 50: return "MEDIUM"
        elif score >= 30: return "LOW"
        else: return "MINIMAL"

    def run_analysis(self):
        self.load_data()
        results = []
        for role in self.roles_data:
            base = self.calculate_base_score(role)
            final = self.apply_cti_modifiers(role['title'], base)
            level = self.classify_risk_level(final)
            
            results.append({
                "title": role['title'],
                "department": role['department'],
                "base_risk_score": base,
                "final_risk_score": final,
                "risk_level": level
            })
        return sorted(results, key=lambda x: x['final_risk_score'], reverse=True)
```

---

## 📊 Task 4: Analysis Execution

### ▶️ File: run_analysis.py

Create the automation orchestration script:

```bash
nano run_analysis.py
```

Paste this implementation containing report writing and metric visualization code:

```python
import json
import pandas as pd
import matplotlib.pyplot as plt
from role_risk_analyzer import RoleRiskAnalyzer

def main():
    analyzer = RoleRiskAnalyzer('organizational_roles.json', 'cti_data.json')
    results = analyzer.run_analysis()

    # Save JSON Report
    with open('risk_report.json', 'w') as f:
        json.dump(results, f, indent=4)

    # Save Text Report
    with open('detailed_risk_report.txt', 'w') as f:
        f.write("========================================\n")
        f.write("      ROLE-BASED RISK REPORT            \n")
        f.write("========================================\n\n")
        for r in results:
            f.write(f"Role: {r['title']} ({r['department']})\n")
            f.write(f" - Base Score: {r['base_risk_score']}\n")
            f.write(f" - Final Score (CTI Adjusted): {r['final_risk_score']}\n")
            f.write(f" - Risk Classification: {r['risk_level']}\n")
            f.write("-" * 40 + "\n")

    # Generate Visualization Charts
    df = pd.DataFrame(results)
    colors = df['risk_level'].map({
        'CRITICAL': 'red', 'HIGH': 'orange', 
        'MEDIUM': 'yellow', 'LOW': 'green', 'MINIMAL': 'lightgray'
    }).fillna('blue')

    plt.figure(figsize=(10, 6))
    plt.bar(df['title'], df['final_risk_score'], color=colors, edgecolor='black')
    plt.ylabel('Final Risk Score')
    plt.title('Organizational Role Risk Profile (With CTI Modifiers)')
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig('risk_analysis_charts.png')
    
    print("[✔] Analysis complete. Generated: risk_report.json, detailed_risk_report.txt, risk_analysis_charts.png")

if __name__ == '__main__':
    main()
```

Run the pipeline execution:

```bash
python3 run_analysis.py
```

---

## 📈 Task 5: Advanced Classification

### 🧠 File: advanced_classifier.py

Create the deep-profiling security recommendations file:

```bash
nano advanced_classifier.py
```

Paste the following compliance control architecture:

```python
import json

class AdvancedClassifier:
    def __init__(self, report_path):
        self.report_path = report_path

    def map_department_multipliers(self, dept):
        multipliers = {"Executive": 1.2, "IT": 1.2, "HR": 1.0, "Sales": 1.1, "Support": 1.0}
        return multipliers.get(dept, 1.0)

    def identify_risk_factors(self, final_score):
        factors = []
        if final_score > 80: factors.append("High system privileges")
        if final_score > 70: factors.append("Sensitive data access")
        if final_score > 60: factors.append("External exposure")
        if final_score > 50: factors.append("Administrative access")
        if final_score > 40: factors.append("Role-based targeting risks")
        return factors

    def get_security_recommendations(self, level):
        if level in ["CRITICAL", "HIGH"]:
            return ["Enable MFA 🔐", "Continuous monitoring 👁️", "Privileged access management 🧾"]
