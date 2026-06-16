# 🛡️ Introduction to Human Risk Assessment 

<div align="center">

# 🎯 Human Risk Assessment in Cybersecurity

### Build a Complete Human Risk Assessment Framework Using Linux, Python, SQLite & Web Technologies

![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)
![Apache](https://img.shields.io/badge/Apache-Web_Server-D22128?style=for-the-badge&logo=apache)
![PHP](https://img.shields.io/badge/PHP-Backend-777BB4?style=for-the-badge&logo=php)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Human_Risk-red?style=for-the-badge)

</div>

---

# 📖 Overview

Human behavior remains one of the largest attack surfaces in modern cybersecurity environments. This lab introduces students to the principles of **Human Risk Assessment (HRA)** by designing and implementing a complete framework that measures, analyzes, and visualizes security-related human behaviors.

Participants will create:

- 📊 Risk Assessment Framework
- 🗄️ SQLite Database Backend
- 🌐 Web-Based Survey Platform
- 🐍 Python Risk Scoring Engine
- 📈 Visualization Dashboard
- 📑 Automated Risk Reports

---

# 🎯 Objectives

By the end of this lab, students will be able to:

✅ Understand fundamental concepts of human risk assessment in cybersecurity

✅ Set up a basic risk assessment framework using open-source tools

✅ Define and identify key risk indicators for human-centered security threats

✅ Create data collection instruments and store assessment data

✅ Analyze risk data to identify security vulnerabilities

---

# 📚 Prerequisites

Before starting this lab, students should have:

- 🐧 Basic understanding of cybersecurity concepts
- 💻 Familiarity with Linux command line operations
- 🐍 Basic knowledge of Python programming
- 🗄️ Understanding of database concepts
- 📖 No prior experience with risk assessment tools required

---

# ☁️ Lab Environment

Al Nafi provides ready-to-use Linux-based cloud machines.

### Environment Includes

- Ubuntu Linux
- Python 3
- SQLite Database
- Apache Web Server
- PHP Runtime
- Pandas & Data Analytics Libraries
- Matplotlib Visualization Tools

No virtual machine setup required.

---

# 🏗️ Task 1 — Set Up Risk Assessment Framework

---

## 🔹 Step 1.1 Create Project Structure

Create a structured environment for the assessment framework.

```bash
# Create main project directory
mkdir -p ~/human-risk-assessment/{framework,data,surveys,reports,scripts}
cd ~/human-risk-assessment

# Create initial configuration files
touch framework/risk-framework.md
touch framework/risk-indicators.txt
touch data/assessment-data.csv
```

### ✅ Verify Structure

```bash
tree ~/human-risk-assessment
```

Expected Structure:

```text
human-risk-assessment
├── framework
├── data
├── surveys
├── reports
└── scripts
```

---

## 🔹 Step 1.2 Define Risk Framework

Create framework documentation.

```bash
nano framework/risk-framework.md
```

Insert:

```markdown
# Human Risk Assessment Framework

## Risk Categories
1. Behavioral Risks
2. Knowledge Gaps
3. Environmental Factors

## Assessment Methodology
- Data Collection
- Risk Analysis
- Reporting

## Success Metrics
- Response rate >80%
- Risk reduction >25%
- Incident reduction >40%
```

Save:

```text
CTRL + X
Y
ENTER
```

---

## 🔹 Step 1.3 Install Required Tools

Update repositories:

```bash
sudo apt update
```

Install packages:

```bash
sudo apt install -y python3 python3-pip sqlite3
```

Install Python libraries:

```bash
pip3 install pandas matplotlib seaborn numpy
```

Verify installation:

```bash
python3 --version
sqlite3 --version
pip3 list
```

---

## 🔹 Step 1.4 Create Assessment Database

Navigate to data directory:

```bash
cd ~/human-risk-assessment/data
```

Create database:

```bash
sqlite3 assessment.db << 'EOF'
CREATE TABLE participants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id TEXT UNIQUE,
    department TEXT,
    role TEXT,
    experience_years INTEGER,
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE risk_responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    participant_id INTEGER,
    question_id TEXT,
    response_value INTEGER,
    category TEXT,
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (participant_id) REFERENCES participants (id)
);

CREATE TABLE risk_scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    participant_id INTEGER,
    category TEXT,
    score INTEGER,
    risk_level TEXT,
    calculated_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (participant_id) REFERENCES participants (id)
);
.quit
EOF
```

Verify tables:

```bash
sqlite3 assessment.db ".tables"
```

Expected Output:

```text
participants
risk_responses
risk_scores
```

---

# 📊 Task 2 — Define Key Risk Indicators

---

## 🔹 Step 2.1 Create Risk Indicators

Open file:

```bash
nano ~/human-risk-assessment/framework/risk-indicators.txt
```

Add:

```text
Password Security
Email Security
Social Engineering
Device Security
Training Awareness
```

### Sample KRIs

```text
Password reuse frequency
MFA adoption
Phishing click rate
Unauthorized software installations
Training completion rates
```

Save and exit.

---

## 🔹 Step 2.2 Create Risk Scoring Engine

Create Python script:

```bash
nano ~/human-risk-assessment/scripts/risk_scoring.py
```

Add starter code from lab instructions.

Make executable:

```bash
chmod +x ~/human-risk-assessment/scripts/risk_scoring.py
```

Run:

```bash
python3 ~/human-risk-assessment/scripts/risk_scoring.py
```

Expected Output:

```text
Risk scoring system initialized
```

---

## 🔹 Step 2.3 Create Visualization Dashboard

Create dashboard script:

```bash
nano ~/human-risk-assessment/scripts/risk_dashboard.py
```

Paste starter code provided in lab.

Make executable:

```bash
chmod +x ~/human-risk-assessment/scripts/risk_dashboard.py
```

Execute:

```bash
python3 ~/human-risk-assessment/scripts/risk_dashboard.py
```

Expected Output:

```text
Dashboard system initialized
```

---

# 🌐 Task 3 — Create Data Collection Survey

---

## 🔹 Step 3.1 Install Web Server

Install Apache and PHP:

```bash
sudo apt install -y apache2 php libapache2-mod-php
```

Start services:

```bash
sudo systemctl start apache2
sudo systemctl enable apache2
```

Verify:

```bash
systemctl status apache2
```

---

## 🔹 Step 3.2 Create Survey Application

Create survey directory:

```bash
sudo mkdir -p /var/www/html/risk-survey
sudo chown -R $USER:$USER /var/www/html/risk-survey
```

Create HTML page:

```bash
nano /var/www/html/risk-survey/index.html
```

Insert survey template from lab instructions.

---

### Test Survey

Open browser:

```text
http://localhost/risk-survey/
```

Expected Result:

✅ Human Risk Assessment Survey displayed

---

## 🔹 Step 3.3 Create Survey Processing Script

Create PHP processor:

```bash
nano /var/www/html/risk-survey/process_survey.php
```

Insert PHP template from lab instructions.

---

## 🔹 Step 3.4 Configure Permissions

Survey permissions:

```bash
sudo chown -R www-data:www-data /var/www/html/risk-survey
sudo chmod -R 755 /var/www/html/risk-survey
```

Database permissions:

```bash
sudo chown www-data:www-data ~/human-risk-assessment/data/assessment.db
sudo chmod 664 ~/human-risk-assessment/data/assessment.db
```

Access URL:

```text
http://localhost/risk-survey/
```

---

# 📈 Task 4 — Generate and Analyze Sample Data

---

## 🔹 Step 4.1 Create Sample Data Generator

Create script:

```bash
nano ~/human-risk-assessment/scripts/generate_sample_data.py
```

Insert provided starter code.

Run:

```bash
cd ~/human-risk-assessment/scripts

python3 generate_sample_data.py
```

Expected Output:

```text
Generated sample data for 20 participants
```

---

## 🔹 Step 4.2 Analyze Collected Data

Create analysis engine:

```bash
nano ~/human-risk-assessment/scripts/analyze_data.py
```

Insert starter template.

Execute:

```bash
python3 analyze_data.py
```

Expected Output:

```text
Analyzing participant data...
Generating reports...
Analysis complete.
```

---

## 🔹 Step 4.3 View Assessment Results

View report:

```bash
cat ~/human-risk-assessment/reports/summary_report.md
```

List generated files:

```bash
ls -lh ~/human-risk-assessment/reports/
```

Query risk statistics:

```bash
sqlite3 ~/human-risk-assessment/data/assessment.db << 'EOF'
SELECT risk_level, COUNT(*) as count
FROM risk_scores
WHERE category='overall'
GROUP BY risk_level;
.quit
EOF
```

Example Output:

```text
Low Risk      5
Medium Risk   9
High Risk     4
Critical Risk 2
```

---

# 🧪 Verification Checklist

Run the following:

```bash
echo "=== Project Structure ==="
tree ~/human-risk-assessment

echo "=== Database Tables ==="
sqlite3 ~/human-risk-assessment/data/assessment.db ".tables"

echo "=== Apache Status ==="
systemctl status apache2 --no-pager

echo "=== Python Libraries ==="
pip3 list | grep -E "pandas|matplotlib|numpy"

echo "=== Survey URL ==="
echo "http://localhost/risk-survey/"
```

---

# 📊 Expected Outcomes

Upon successful completion:

✅ Risk Assessment Framework Created

✅ SQLite Database Operational

✅ Web-Based Survey Functional

✅ Risk Scoring Engine Developed

✅ Dashboard Templates Created

✅ Sample Assessment Data Generated

✅ Security Risk Reports Produced

---

# 🚨 Troubleshooting

---

## Database Permission Errors

```bash
sudo chown www-data:www-data assessment.db
```

---

## Apache Not Serving Survey

Check status:

```bash
sudo systemctl status apache2
```

Restart service:

```bash
sudo systemctl restart apache2
```

---

## Python Import Errors

Verify packages:

```bash
pip3 list | grep -E "pandas|matplotlib"
```

Install missing libraries:

```bash
pip3 install pandas matplotlib seaborn numpy
```

---

## Empty Survey Responses

Check Apache logs:

```bash
sudo tail -f /var/log/apache2/error.log
```

---

# 🎓 Conclusion

In this lab you successfully built a foundational **Human Risk Assessment Platform** using Linux, Python, SQLite, Apache, and PHP.

### Skills Acquired

🔹 Human Risk Assessment Framework Design

🔹 Cybersecurity Risk Indicator Development

🔹 Database Design and Data Collection

🔹 Web-Based Survey Creation

🔹 Python-Based Risk Analytics

🔹 Security Data Visualization

🔹 Reporting and Risk Communication

### Why This Matters

Human error remains one of the most significant contributors to cybersecurity incidents. Understanding how to assess, quantify, and mitigate human risk enables organizations to:

- 🛡️ Improve Security Awareness
- 📊 Measure Security Culture
- 🎯 Prioritize Training Initiatives
- 📉 Reduce Security Incidents
- 🏢 Strengthen Organizational Resilience

The framework developed in this lab serves as the foundation for advanced human-centric cybersecurity programs and enterprise security awareness initiatives.

---

<div align="center">

# 🏆 Lab Completed Successfully

### Human Risk Assessment Framework Deployment & Analysis

⭐ Continue to Advanced Human Risk Analytics Labs

</div>
