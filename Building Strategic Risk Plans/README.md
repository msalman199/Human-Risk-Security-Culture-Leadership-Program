# 🛡️ Building Strategic Risk Plans Lab

![Python](https://shields.io)
![Risk](https://shields.io)
![Security](https://shields.io)
![Lab](https://shields.io)

---

## 📌 Overview

This lab focuses on building a **Strategic Risk Management Framework** that connects:

- 🧠 Cybersecurity risks
- 👥 Human behavior patterns
- 🏢 Organizational culture
- 📊 Data-driven decision making

You will develop Python tools to:
- Analyze risk behavior alignment
- Build role-based risk models
- Create prioritization frameworks
- Generate reports & visualizations

---

## 🎯 Objectives

By the end of this lab, you will be able to:

- 🏗️ Design a strategic risk management framework
- 🐍 Implement role-based risk assessments using Python
- 📊 Create prioritization matrices for security decisions
- 📈 Build automated risk visualization tools
- 📑 Generate enterprise-level risk management reports

---

## ⚙️ Prerequisites

- 🐍 Python basics (functions, loops, dictionaries, file handling)
- 🛡️ Understanding of cybersecurity risk concepts
- 🐧 Linux command line familiarity
- 🏢 Basic knowledge of organizational roles & security

---

## 💻 Lab Environment

This lab runs on **Al Nafi Cloud Linux Machines ☁️**

👉 Click **Start Lab** to access:
- Python 3 environment
- Pre-installed libraries
- Ready-to-use workspace

---

## 📁 Project Structure

```text
risk_management_lab/
│
├── risk_framework.py
├── risk_visualization.py
├── role_risk_assessment.py
├── role_visualization.py
├── risk_report_generator.py
├── risk_alignment_matrix.csv
├── risk_management_report.json
└── risk_report.md
```

---

## 🚀 Task 1: Risk Framework Setup

### 🔹 Create Environment

```bash
mkdir ~/risk_management_lab
cd ~/risk_management_lab
python3 --version
pip3 install pandas matplotlib seaborn numpy
```

---

## 🧠 Task 2: Risk-Behavior-Culture Framework

### 📄 File: risk_framework.py

This module builds the foundation of strategic risk analysis.

```bash
nano risk_framework.py
```

Paste the core engine implementation:

```python
import json
import pandas as pd
import numpy as np

class RiskFramework:
    def __init__(self):
        self.risk_categories = {
            "Phishing": {"severity": 8, "base_multiplier": 1.2},
            "Weak Passwords": {"severity": 5, "base_multiplier": 1.0},
            "Social Engineering": {"severity": 9, "base_multiplier": 1.3},
            "Insider Threats": {"severity": 10, "base_multiplier": 1.5},
            "Unsecured Devices": {"severity": 6, "base_multiplier": 1.1}
        }
        self.behavior_patterns = {"Low": 0.8, "Medium": 1.2, "High": 1.6}
        self.culture_factors = {
            "Leadership Commitment": 0.4,
            "Employee Engagement": 0.5,
            "Communication Effectiveness": 0.6,
            "Learning Culture": 0.7,
            "Accountability Structure": 0.8
        }

    def calculate_risk_score(self, risk_type, behavior_level, culture_score):
        if risk_type not in self.risk_categories:
            return 0.0
        
        severity = self.risk_categories[risk_type]["severity"]
        base_mult = self.risk_categories[risk_type]["base_multiplier"]
        behavior_mult = self.behavior_patterns.get(behavior_level, 1.0)
        
        # Risk Score = Severity × Behavior Multiplier × Culture Impact
        # Culture impact acts inversely: lower score increases risk impact
        culture_impact = 1.5 - culture_score 
        
        score = severity * (base_mult * behavior_mult) * culture_impact
        return round(float(score), 2)

    def generate_matrix(self):
        matrix_data = []
        culture_values = [0.3, 0.5, 0.7, 0.9]
        
        for risk, attrs in self.risk_categories.items():
            for b_level in self.behavior_patterns.keys():
                for c_score in culture_values:
                    score = self.calculate_risk_score(risk, b_level, c_score)
                    matrix_data.append({
                        "Risk Type": risk,
                        "Behavior Level": b_level,
                        "Culture Score": c_score,
                        "Calculated Risk Score": score
                    })
                    
        df = pd.DataFrame(matrix_data)
        df.to_csv("risk_alignment_matrix.csv", index=False)
        
        with open("risk_framework_data.json", "w") as f:
            json.dump(matrix_data, f, indent=4)
        print("[✔] Framework calculation done. Saved matrix dataset outputs.")

if __name__ == "__main__":
    rf = RiskFramework()
    rf.generate_matrix()
```

---

## 📊 Task 3 & 4: Risk Visualization Module

### 📄 File: risk_visualization.py

```bash
nano risk_visualization.py
```

Paste the analytics graphics pipeline code:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def build_visualizations():
    try:
        df = pd.read_csv("risk_alignment_matrix.csv")
    except FileNotFoundError:
        print("[❌] Run risk_framework.py first!")
        return

    sns.set_theme(style="whitegrid")
    
    # 1. Risk Heatmap Configuration
    plt.figure(figsize=(10, 6))
    pivot_df = df.pivot_table(index="Risk Type", columns="Behavior Level", values="Calculated Risk Score", aggfunc='mean')
    sns.heatmap(pivot_df, annot=True, cmap="YlOrRd", fmt=".1f", linewidths=.5)
    plt.title("Risk Heatmap: Risk Type vs Behavior Level")
    plt.tight_layout()
    plt.savefig("risk_heatmap.png")
    plt.close()

    # 2. Culture Impact Chart Configuration
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x="Culture Score", y="Calculated Risk Score", hue="Risk Type", marker="o")
    plt.title("Culture Impact Graph: Score Decays vs Risk Manifestation")
    plt.ylabel("Risk Metric Output")
    plt.tight_layout()
    plt.savefig("culture_impact_graph.png")
    plt.close()
    
    print("[✔] Visualizations built successfully: risk_heatmap.png, culture_impact_graph.png")

if __name__ == "__main__":
    build_visualizations()
```

---

## 🧑‍💼 Task 5 & 6: Role-Based Risk Assessment

### 📄 File: role_risk_assessment.py

```bash
nano role_risk_assessment.py
```

Paste the priority infrastructure calculations code:

```python
import json

class RoleRiskAssessor:
    def __init__(self):
        self.roles = {
            "Executive": {"weight": 0.95, "primary_risk": "Social Engineering"},
            "IT Administrator": {"weight": 0.90, "primary_risk": "Insider Threats"},
            "Finance": {"weight": 0.80, "primary_risk": "Phishing"},
            "General Staff": {"weight": 0.50, "primary_risk": "Weak Passwords"}
        }
        self.dimensions = ["Financial impact", "Operational disruption", "Reputational damage", "Legal exposure"]

    def determine_priority_and_action(self, score):
        if score >= 8.0:
            return "CRITICAL", "Immediate action needed (1–2 weeks). Deploy isolating containment architecture & PAM constraints."
        elif score >= 6.0:
            return "HIGH", "Remediation target within 1 month. Mandate dynamic behavioral authentication."
        elif score >= 4.0:
            return "MEDIUM", "Remediation target within 3 months. Conduct target phishing drills."
        else:
            return "LOW", "Monitor and update within 6 months. Distribute general awareness training modules."

    def assess_roles(self):
        assessments = []
        base_dimension_score = 5.0  # Normalized structural anchor
        
        for role, properties in self.roles.items():
            weight = properties["weight"]
            primary = properties["primary_risk"]
            
            # Risk Scoring Factor Logic Execution
            raw_score = base_dimension_score * weight
            amplified_score = raw_score * 1.3 # Primary risk factor modifier
            final_score = round(min(amplified_score, 10.0), 2)
            
            level, plan = self.determine_priority_and_action(final_score)
            
            assessments.append({
                "Role": role,
                "Assigned Weight": weight,
                "Primary Threat Context": primary,
                "Aggregated Risk Score": final_score,
                "Priority Level": level,
                "Action Strategy Plan": plan
            })
            
        with open("role_assessment_outputs.json", "w") as f:
            json.dump(assessments, f, indent=4)
        print("[✔] Role assessment and action plan engine execution completed.")

if __name__ == "__main__":
    rra = RoleRiskAssessor()
    rra.assess_roles()
```

---

## 📊 Task 7: Role-Based Visualization

### 📄 File: role_visualization.py

```bash
nano role_visualization.py
```

Paste the role chart compilation processing model logic:

```python
import json
import matplotlib.pyplot as plt

def build_role_charts():
    try:
        with open("role_assessment_outputs.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("[❌] Execute role_risk_assessment.py first!")
        return

    roles = [item["Role"] for item in data]
    scores = [item["Aggregated Risk Score"] for item in data]
    colors = ['red' if s >= 8.0 else 'orange' if s >= 6.0 else 'yellow' if s >= 4.0 else 'green' for s in scores]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(roles, scores, color=colors, edgecolor='grey')
