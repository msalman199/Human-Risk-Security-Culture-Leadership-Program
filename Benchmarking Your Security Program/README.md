# 🛡️ Benchmarking Your Security Program 

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Security](https://img.shields.io/badge/Security-Benchmarking-red)
![Maturity](https://img.shields.io/badge/Maturity-Model-orange)
![Lab](https://img.shields.io/badge/Status-Hands%20On-success)

---

## 📌 Overview

This lab focuses on **Security Program Benchmarking**, helping you evaluate the **maturity of an organization’s security program** using structured models and automated Python tools.

You will learn how to:

- 📊 Measure security maturity using standardized frameworks
- 🧠 Analyze governance, risk, and technical controls
- 🐍 Automate benchmarking with Python
- 📈 Generate reports and visual insights
- 🚀 Identify improvement opportunities

---

## 🎯 Objectives

By the end of this lab, you will be able to:

- 🏗️ Understand security maturity assessment frameworks
- ⚙️ Configure benchmarking environments on Linux
- 📊 Analyze security program maturity using metrics
- 🐍 Develop Python automation scripts
- 📑 Generate maturity reports and recommendations

---

## ⚙️ Prerequisites

- 🐧 Linux command-line basics
- 🐍 Python fundamentals (loops, functions, file handling)
- 🛡️ Knowledge of cybersecurity frameworks (NIST / ISO 27001)
- 🏢 Understanding of security governance concepts

---

## 💻 Lab Environment

This lab runs on **Ubuntu 22.04 LTS (Al Nafi Cloud Machines ☁️)**

You will have:
- Python 3.10 🐍
- pip package manager 📦
- nano / vim editors ✍️
- Internet access 🌐

---

## 📁 Project Structure

```text
security-benchmark/
│
├── config/
│   └── framework.yaml
│
├── data/
│   ├── questions.yaml
│   └── sample_responses.yaml
│
├── scripts/
│   ├── benchmark_analyzer.py
│   ├── report_generator.py
│   ├── run_benchmark.py
│   ├── interactive_assessment.py
│   └── compare_assessments.py
│
└── reports/
    ├── assessment_report.md
    ├── domain_scores.png
    └── recommendations.txt
```

---

## 🚀 Task 1: Environment Setup

### 🔹 System Preparation

```bash
sudo apt update && sudo apt install python3-pip python3-venv -y
mkdir -p ~/security-benchmark/config ~/security-benchmark/data ~/security-benchmark/scripts ~/security-benchmark/reports
cd ~/security-benchmark
python3 -m venv venv
source venv/bin/activate
```

### 🔹 Install Dependencies

```bash
pip install pandas pyyaml matplotlib seaborn
pip freeze > requirements.txt
```

---

## ⚙️ Task 2: Framework Configuration

### 📄 File: config/framework.yaml

```bash
nano config/framework.yaml
```

Paste the following framework configuration setup:

```yaml
framework:
  name: "Custom Security Maturity Model"
  version: "1.0"
  domains:
    governance:
      weight: 0.25
      description: "🏛️ Governance policies, structural alignment, and strategic oversight."
    risk_management:
      weight: 0.20
      description: "⚠️ Risk identification, treatment matrices, and risk appetite."
    incident_response:
      weight: 0.15
      description: "🚨 Response execution, playbook readiness, and containment plans."
    awareness:
      weight: 0.15
      description: "🎓 Targeted employee educational courses and training operations."
    technical_controls:
      weight: 0.25
      description: "🔧 Technical boundary safeguards, IAM controls, and data protection."
  maturity_levels:
    1: "Initial"
    2: "Developing"
    3: "Defined"
    4: "Managed"
    5: "Optimized"
```

---

## 📋 Task 3: Assessment Questions

### 📄 File: data/questions.yaml

```bash
nano data/questions.yaml
```

Paste the framework operational checklist questions:

```yaml
questions:
  - id: G1
    domain: "governance"
    text: "Are formal cybersecurity policies approved by leadership and updated annually?"
  - id: R1
    domain: "risk_management"
    text: "Is there an established corporate IT asset risk registration methodology?"
  - id: I1
    domain: "incident_response"
    text: "Does the enterprise have dedicated incident response communication playbooks?"
  - id: A1
    domain: "awareness"
    text: "Are employees subjected to periodic targeted phishing simulations?"
  - id: T1
    domain: "technical_controls"
    text: "Is Multi-Factor Authentication (MFA) fully enforced for all administrative system endpoints?"
```

---

## 🧪 Task 4: Sample Assessment Data

### 📄 File: data/sample_responses.yaml

```bash
nano data/sample_responses.yaml
```

Paste the initial organizational response simulation data:

```yaml
assessment:
  organization: "TechCorp Inc"
  industry: "Technology"
  date: "2026-06-16"
  responses:
    G1: 3
    R1: 2
    I1: 4
    A1: 2
    T1: 5
```

---

## 🧠 Task 5: Benchmark Analyzer

### 📄 File: scripts/benchmark_analyzer.py

```bash
nano scripts/benchmark_analyzer.py
```

Paste the data compilation engine script:

```python
import yaml
import os

class BenchmarkAnalyzer:
    def __init__(self, framework_path, questions_path):
        with open(framework_path, 'r') as f:
            self.framework = yaml.safe_load(f)['framework']
        with open(questions_path, 'r') as f:
            self.questions = yaml.safe_load(f)['questions']

    def calculate_scores(self, responses_path):
        with open(responses_path, 'r') as f:
            data = yaml.safe_load(f)['assessment']
            
        responses = data['responses']
        domain_sums = {domain: 0 for domain in self.framework['domains']}
        domain_counts = {domain: 0 for domain in self.framework['domains']}
        
        for q in self.questions:
            q_id = q['id']
            domain = q['domain']
            if q_id in responses:
                # Map 1-5 response metric onto a 0-100% scale score
                domain_sums[domain] += (responses[q_id] / 5.0) * 100
                domain_counts[domain] += 1
                
        domain_scores = {}
        overall_score = 0.0
        
        for domain, weight in self.framework['domains'].items():
            count = domain_counts.get(domain, 0)
            score = (domain_sums[domain] / count) if count > 0 else 0.0
            domain_scores[domain] = round(score, 2)
            overall_score += score * weight['weight']
            
        # Overall Score = Weighted Average(Domain Scores) mapped back to Level 1-5 scale
        calculated_level = round((overall_score / 100) * 5)
        maturity_label = self.framework['maturity_levels'].get(calculated_level, "Unknown")
        
        return {
            "organization": data['organization'],
            "industry": data['industry'],
            "date": data['date'],
            "domain_scores": domain_scores,
            "overall_score": round(overall_score, 2),
            "maturity_level": calculated_level,
            "maturity_label": maturity_label
        }
```

---

## 📊 Task 6: Report Generator

### 📄 File: scripts/report_generator.py

```bash
nano scripts/report_generator.py
```

Paste the file compiler documentation generator:

```python
import matplotlib.pyplot as plt
import os

class ReportGenerator:
    @staticmethod
    def generate_visuals(scores, output_path):
        domains = list(scores.keys())
        values = list(scores.values())
        
        plt.figure(figsize=(8, 5))
        plt.bar(domains, values, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], edgecolor='black')
        plt.ylabel('Maturity Percentage Level (%)')
        plt.title('Security Maturity Baseline Domain Metric Analysis')
        plt.ylim(0, 100)
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()

    @staticmethod
    def write_markdown_report(metrics, md_path, rec_path):
        # 💡 Security Recommendations mapping
        recommendations = []
        for domain, score in metrics['domain_scores'].items():
            if score < 50:
                recommendations.append(f"[-] Critical Action required in [{domain.upper()}]. Score is below 50%. Enforce formal control mappings.")
            elif score < 75:
                recommendations.append(f"[!] Optimization suggested in [{domain.upper()}]. Refine existing procedural execution parameters.")
            else:
                recommendations.append(f"[+] Maintain robust controls in [{domain.upper()}]. Continuous automation audits recommended.")

        # Save Text Recommendations
        with open(rec_path, 'w') as f:
            f.write("\n".join(recommendations))

        # Generate Full Markdown Report Structure
        report_md = f"""# 📈 Security Maturity Benchmarking Report

## 🏛️ Executive Summary
- **Organization**: {metrics['organization']}
- **Vertical Sector**: {metrics['industry']}
- **Assessment Audit Date**: {metrics['date']}
- **Overall Aggregated Security Index Score**: {metrics['overall_score']} / 100%
- **Assessed Framework Maturity Level**: {metrics['maturity_level']} ({metrics['maturity_label']})

## 📊 Domain Performance Indexes
"""
        for d, s in metrics['domain_scores'].items():
            report_md += f"- **{d.replace('_', ' ').title()} Index**: {s}%\n"

        report_md += "\n## 💡 Targeted Control Adjustments Actions\n"
        for rec in recommendations:
            report_md += f"{rec}\n"

        with open(md_path, 'w') as f:
            f.write(report_md)
```

---

## 🧑‍💻 Task 7: Execution Script

### 📄 File: scripts/run_benchmark.py

```bash
nano scripts/run_benchmark.py
```
