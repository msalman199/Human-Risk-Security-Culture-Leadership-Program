# 🎯 Segmenting Audiences for Security Training

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![CSV](https://img.shields.io/badge/CSV-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Security](https://img.shields.io/badge/Cybersecurity-Training-red?style=for-the-badge&logo=shield&logoColor=white)

![License](https://img.shields.io/badge/License-Educational-blue?style=flat-square)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Model](https://img.shields.io/badge/Model-AIDA-purple?style=flat-square)

> *Build a Python-based audience segmentation and personalized messaging system for cybersecurity training — powered by the AIDA model.*

</div>

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [✅ Prerequisites](#-prerequisites)
- [🖥️ Lab Environment](#️-lab-environment)
- [👥 Task 1 — Employee Data & Segmentation](#-task-1-create-employee-data-and-segmentation-system)
- [📣 Task 2 — AIDA Model Messaging](#-task-2-implement-aida-model-for-targeted-messaging)
- [🧪 Task 3 — Test & Validate](#-task-3-test-and-validate-segmentation-system)
- [🏆 Expected Outcomes](#-expected-outcomes)
- [🐛 Troubleshooting](#-troubleshooting-tips)
- [📌 Key Takeaways](#-key-takeaways)

---

## 🎯 Objectives

By the end of this lab, students will be able to:

- 🐍 Implement **Python-based audience segmentation** for cybersecurity training programs
- 🏷️ Categorize employees by **role, location, and risk factors**
- 📣 Apply the **AIDA model** (Attention, Interest, Desire, Action) to create targeted messages
- 🎯 Generate **personalized training recommendations** based on employee profiles
- 📊 Analyze **segmentation effectiveness** for training optimization

---

## ✅ Prerequisites

| Requirement | Details |
|---|---|
| 🐍 Python | Basic programming (functions, dictionaries, lists) |
| 📄 CSV | Understanding of CSV file operations |
| 🔐 Cybersecurity | Familiarity with cybersecurity concepts |
| ✏️ Text Editor | Text editor or Python IDE access |

---

## 🖥️ Lab Environment

> **Al Nafi** provides Linux-based cloud machines for this lab.
> Click **Start Lab** to access your pre-configured environment.

Your lab machine includes:

| Tool | Version/Details |
|---|---|
| 🐍 Python | 3.8+ |
| 📦 Standard Libraries | csv, json, collections |
| ✏️ Text Editors | nano, vim |

---

## 👥 Task 1: Create Employee Data and Segmentation System

### 📁 Step 1 — Set Up Lab Directory

Create your working directory and verify Python installation:

```bash
mkdir ~/security_training_lab
cd ~/security_training_lab
python3 --version
```

### 🗂️ Step 2 — Generate Sample Employee Data

Create `employee_data_generator.py`:

```python
#!/usr/bin/env python3
"""
Employee Data Generator for Security Training Segmentation
Students: Complete the TODO sections to generate employee data
"""

import csv
import random

def generate_employee_data(num_employees=200):
    """
    Generate sample employee data with security-relevant attributes.

    Args:
        num_employees: Number of employee records to generate

    Returns:
        List of employee dictionaries
    """
    departments = ['IT', 'Finance', 'HR', 'Marketing', 'Operations', 'Legal', 'Executive']

    roles = {
        'IT':        ['System Administrator', 'Developer', 'Security Analyst', 'Network Engineer'],
        'Finance':   ['Accountant', 'Financial Analyst', 'Controller', 'CFO'],
        'HR':        ['HR Specialist', 'Recruiter', 'HR Manager', 'Benefits Coordinator'],
        'Marketing': ['Marketing Specialist', 'Content Creator', 'Marketing Manager'],
        'Operations':['Operations Manager', 'Project Manager', 'Quality Analyst'],
        'Legal':     ['Legal Counsel', 'Compliance Officer', 'Contract Manager'],
        'Executive': ['CEO', 'CTO', 'VP Sales', 'VP Operations']
    }

    locations         = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    access_levels     = ['Low', 'Medium', 'High', 'Critical']
    training_history  = ['Never', 'Over 1 year ago', '6-12 months ago', 'Within 3 months']
    incident_history  = ['None', 'Minor', 'Moderate', 'Severe']

    employees = []

    for i in range(1, num_employees + 1):
        dept = random.choice(departments)

        # TODO: Create employee dictionary with all required fields
        # TODO: Calculate risk_score based on access_level, training_history, and incident_history
        # TODO: Add department-specific risk adjustments
        # Hint: Risk score should range from 1-12

        employee = {
            'employee_id':      f'EMP{i:03d}',
            'name':             f'Employee {i}',
            'department':       dept,
            'role':             random.choice(roles[dept]),
            'location':         random.choice(locations),
            'access_level':     random.choice(access_levels),
            'last_training':    random.choice(training_history),
            'incident_history': random.choice(incident_history),
            'years_experience': random.randint(1, 20),
            'risk_score':       0  # TODO: Calculate this value
        }

        employees.append(employee)

    return employees

def save_to_csv(employees, filename='employees.csv'):
    """
    Save employee data to CSV file.

    Args:
        employees: List of employee dictionaries
        filename:  Output CSV filename
    """
    # TODO: Implement CSV writing logic
    # TODO: Use csv.DictWriter with appropriate fieldnames
    pass

if __name__ == "__main__":
    print("Generating employee data...")
    # TODO: Call generate_employee_data() and save_to_csv()
    # TODO: Print confirmation message
```

> 📌 **Student Task:** Complete the TODOs to generate 200 employee records with calculated risk scores.

### 🔀 Step 3 — Implement Segmentation Logic

Create `audience_segmentation.py`:

```python
#!/usr/bin/env python3
"""
Audience Segmentation System for Security Training
Students: Implement segmentation methods
"""

import csv
from collections import defaultdict, Counter

class SecurityTrainingSegmentation:
    def __init__(self, csv_file='employees.csv'):
        """Initialize segmentation system and load employee data."""
        self.employees = []
        self.segments  = {}
        self.load_employee_data(csv_file)

    def load_employee_data(self, csv_file):
        """
        Load employee data from CSV file.

        Args:
            csv_file: Path to employee CSV file
        """
        # TODO: Implement CSV reading
        # TODO: Convert numeric fields (years_experience, risk_score) to integers
        # TODO: Store in self.employees list
        pass

    def segment_by_department(self):
        """
        Segment employees by department.

        Returns:
            Dictionary with department as key, employee list as value
        """
        # TODO: Create defaultdict to group employees by department
        # TODO: Iterate through self.employees and categorize
        # TODO: Store in self.segments['department']
        pass

    def segment_by_risk_level(self):
        """
        Segment employees by risk score into four categories.

        Returns:
            Dictionary with risk categories and employee lists
        """
        risk_segments = {
            'Low Risk (1-3)':      [],
            'Medium Risk (4-6)':   [],
            'High Risk (7-9)':     [],
            'Critical Risk (10-12)':[]
        }

        # TODO: Categorize each employee based on risk_score
        # TODO: Store in self.segments['risk']
        pass

    def segment_by_training_urgency(self):
        """
        Calculate training urgency based on multiple factors.

        Returns:
            Dictionary with urgency levels and employee lists
        """
        urgency_segments = {
            'Immediate':       [],
            'High Priority':   [],
            'Medium Priority': [],
            'Low Priority':    []
        }

        # TODO: Calculate urgency_score for each employee
        # TODO: Consider: risk_score, last_training, incident_history, access_level
        # TODO: Categorize based on total urgency score
        # Hint: Immediate >= 15, High >= 10, Medium >= 6, Low < 6
        pass

    def generate_segment_report(self):
        """Generate and print comprehensive segmentation report."""
        # TODO: Print total employee count
        # TODO: Print department distribution with percentages
        # TODO: Print risk level distribution
        # TODO: Print training urgency distribution
        pass

    def export_segments_to_csv(self):
        """Export each segment to separate CSV files."""
        # TODO: Iterate through self.segments
        # TODO: Create CSV file for each non-empty segment
        # TODO: Use naming convention: segment_{type}_{name}.csv
        pass

def main():
    """Main function to run segmentation analysis."""
    # TODO: Initialize SecurityTrainingSegmentation
    # TODO: Call all segmentation methods
    # TODO: Generate report
    # TODO: Export segments to CSV
    pass

if __name__ == "__main__":
    main()
```

> 📌 **Student Task:** Implement all segmentation methods and generate a comprehensive report.

---

## 📣 Task 2: Implement AIDA Model for Targeted Messaging

### ✉️ Step 1 — Create AIDA Message Templates

Create `aida_messaging.py`:

```python
#!/usr/bin/env python3
"""
AIDA Model Implementation for Security Training Messages
Students: Complete message generation logic
"""

import csv
import json
from datetime import datetime

class AidaMessageGenerator:
    def __init__(self):
        """Initialize AIDA message generator with templates."""
        self.message_templates = self.create_message_templates()

    def create_message_templates(self):
        """
        Create AIDA message templates for different audience segments.

        Returns:
            Dictionary of message templates by category
        """
        templates = {
            'high_risk_executives': {
                'attention': "URGENT: Executive Security Alert - You Are a Prime Target",
                'interest':  "As a senior executive, you handle sensitive information and make critical decisions. Cybercriminals specifically target executives for their access privileges.",
                'desire':    "Protect your reputation and company assets by mastering advanced security practices. Join executives who have strengthened their security posture.",
                'action':    "Schedule your executive security briefing within 48 hours. Contact security@company.com."
            },
            'high_risk_it': {
                'attention': "Critical Security Update Required for IT Personnel",
                'interest':  "Your technical access makes you both an asset and a potential attack vector. Recent threats target IT professionals through sophisticated exploits.",
                'desire':    "Stay ahead of emerging threats with advanced technical security training tailored for IT professionals.",
                'action':    "Complete IT security certification within 7 days at training.company.com/it-security."
            },
            # TODO: Add templates for:
            # - medium_risk_finance
            # - low_risk_general
            # - never_trained
            # - incident_history
        }
        return templates

    def determine_message_category(self, employee):
        """
        Determine appropriate AIDA template based on employee profile.

        Args:
            employee: Employee dictionary with profile data

        Returns:
            String indicating message category
        """
        # TODO: Implement priority-based categorization logic
        # TODO: Check incident_history first (highest priority)
        # TODO: Check if never_trained
        # TODO: Check department and risk_score combinations
        # TODO: Return appropriate category string
        pass

    def generate_personalized_message(self, employee):
        """
        Generate personalized AIDA message for an employee.

        Args:
            employee: Employee dictionary

        Returns:
            Dictionary with personalized message components
        """
        category = self.determine_message_category(employee)
        template = self.message_templates[category]

        # TODO: Create personalized_message dictionary with:
        # - employee_id, employee_name, department, role, risk_score
        # - message_category, generated_date
        # - aida_components (attention, interest, desire, action)
        # - full_message (formatted complete message)
        pass

    def personalize_interest(self, interest_template, employee):
        """
        Add personalization to interest section based on experience.

        Args:
            interest_template: Base interest message
            employee:          Employee dictionary

        Returns:
            Personalized interest message
        """
        # TODO: Add experience-based context
        # TODO: < 2 years:  mention being new
        # TODO: > 10 years: mention extensive experience
        # TODO: else:       mention being security advocate
        pass

    def format_full_message(self, template, employee):
        """
        Format complete AIDA message with all components.

        Args:
            template: AIDA template dictionary
            employee: Employee dictionary

        Returns:
            Formatted string message
        """
        # TODO: Create formatted message with:
        # - Greeting with employee name
        # - All AIDA components (Attention, Interest, Desire, Action)
        # - Context about role and department
        # - Signature
        pass

    def export_messages_for_delivery(self, messages, output_file):
        """
        Export messages in email-ready CSV format.

        Args:
            messages:    List of message dictionaries
            output_file: Output CSV filename
        """
        # TODO: Create CSV with columns: employee_id, employee_name, email_subject, email_body, priority
        # TODO: Map message categories to priority levels (High/Medium/Low)
        # TODO: Write all messages to CSV
        pass

def main():
    """Main function to generate AIDA messages."""
    # TODO: Initialize AidaMessageGenerator
    # TODO: Load employees from CSV
    # TODO: Generate message for each employee
    # TODO: Save messages to JSON file
    # TODO: Export for email delivery
    # TODO: Display sample messages from different categories
    pass

if __name__ == "__main__":
    main()
```

> 📌 **Student Task:** Complete the AIDA message generation system with personalization logic.

### 📊 Step 2 — Create Message Analysis Tool

Create `message_analysis.py`:

```python
#!/usr/bin/env python3
"""
Message Analysis Tool for Security Training
Students: Implement analysis methods
"""

import json
from collections import Counter, defaultdict

class MessageAnalyzer:
    def __init__(self, messages_file='aida_messages.json'):
        """Initialize message analyzer."""
        self.messages = []
        self.load_messages(messages_file)

    def load_messages(self, messages_file):
        """
        Load messages from JSON file.

        Args:
            messages_file: Path to messages JSON file
        """
        # TODO: Load JSON file into self.messages
        # TODO: Handle FileNotFoundError
        pass

    def analyze_message_distribution(self):
        """
        Analyze distribution of message categories.

        Returns:
            Counter object with category counts
        """
        # TODO: Count messages by category
        # TODO: Calculate and print percentages
        # TODO: Return Counter object
        pass

    def analyze_by_department(self):
        """
        Analyze message categories by department.

        Returns:
            Nested dictionary: department -> category -> count
        """
        # TODO: Create nested defaultdict structure
        # TODO: Count messages by department and category
        # TODO: Print analysis with percentages
        pass

    def analyze_risk_correlation(self):
        """
        Analyze correlation between risk scores and message categories.

        Returns:
            Dictionary mapping categories to risk score lists
        """
        # TODO: Group risk scores by message category
        # TODO: Calculate average, min, max for each category
        # TODO: Print statistical analysis
        pass

    def generate_training_recommendations(self):
        """
        Generate actionable training recommendations.

        Returns:
            List of recommendation dictionaries
        """
        recommendations = []

        # TODO: Analyze message categories
        # TODO: Create recommendations for:
        #   - High-risk personnel (immediate action)
        #   - Incident history (refresher training)
        #   - Never trained (onboarding)
        #   - Department-specific needs
        # TODO: Include priority, count, recommendation text, timeline
        pass

    def export_recommendations(self, recommendations, output_file):
        """
        Export recommendations to CSV file.

        Args:
            recommendations: List of recommendation dictionaries
            output_file:     Output CSV filename
        """
        # TODO: Write recommendations to CSV
        # TODO: Include all recommendation fields
        pass

def main():
    """Main function to run message analysis."""
    # TODO: Initialize MessageAnalyzer
    # TODO: Run all analysis methods
    # TODO: Generate recommendations
    # TODO: Export recommendations to CSV
    # TODO: Print summary statistics
    pass

if __name__ == "__main__":
    main()
```

> 📌 **Student Task:** Implement analysis methods to evaluate message effectiveness and generate recommendations.

---

## 🧪 Task 3: Test and Validate Segmentation System

### ▶️ Step 1 — Run Complete Workflow

Execute the complete segmentation and messaging workflow:

```bash
# Generate employee data
python3 employee_data_generator.py

# Run segmentation analysis
python3 audience_segmentation.py

# Generate AIDA messages
python3 aida_messaging.py

# Analyze message effectiveness
python3 message_analysis.py
```

### 📂 Step 2 — Verify Output Files

Check that all expected files are created:

```bash
ls -lh *.csv *.json
```

Expected files:

| File | Description |
|---|---|
| `employees.csv` | Original employee data |
| `segment_*.csv` | Segmented employee groups |
| `aida_messages.json` | Generated messages |
| `messages_for_delivery.csv` | Email-ready messages |
| `training_recommendations.csv` | Action items |

### 🔍 Step 3 — Review Sample Outputs

Examine segmentation results:

```bash
# View first 10 employees
head -n 11 employees.csv

# Count employees by segment
wc -l segment_*.csv

# View sample message
head -n 30 messages_for_delivery.csv
```

---

## 🏆 Expected Outcomes

Upon successful completion, students will have:

| ✅ Deliverable | Description |
|---|---|
| 👥 Employee Dataset | 200 records including calculated risk scores |
| 🔀 Segmentation System | Employees categorized by department, risk, and urgency |
| ✉️ AIDA Messages | Personalized messages for each employee segment |
| 📊 Analysis Reports | Distribution and correlation analysis |
| 📋 Recommendations | Training priorities with timelines |

Key metrics to observe:

- 📈 Risk distribution across departments
- 🎯 Message category alignment with risk levels
- ⏱️ Training urgency prioritization
- 🤝 Personalization effectiveness

---

## 🐛 Troubleshooting Tips

### ⚠️ Issue: CSV File Not Found Errors

> **Solution:** Ensure scripts run in correct order (data generator first).

```bash
# Always run data generator first
python3 employee_data_generator.py

# Then verify file exists
ls -lh employees.csv
```

### ⚠️ Issue: Risk Scores All Zero or Incorrect

> **Solution:** Check risk calculation logic in `employee_data_generator.py`.

```python
# Verify all factors are considered:
# - access_level
# - training_history
# - incident_history
# Hint: Risk score should range from 1-12
```

### ⚠️ Issue: Messages Not Personalized

> **Solution:** Review `determine_message_category()` logic.

```python
# Ensure employee attributes are correctly accessed
# Check keys match CSV column names exactly
```

### ⚠️ Issue: Empty Segment Files

> **Solution:** Verify segmentation thresholds are appropriate.

```python
# Check that employees exist in each category
# Adjust thresholds if distribution is uneven
# Immediate >= 15, High >= 10, Medium >= 6, Low < 6
```

---

## 📌 Key Takeaways

```
╔══════════════════════════════════════════════════════════════╗
║                     KEY TAKEAWAYS                           ║
╠══════════════════════════════════════════════════════════════╣
║  🎯  Segmentation improves training relevance               ║
║  🚨  Risk-based prioritization ensures critical personnel   ║
║      receive immediate attention                            ║
║  📣  AIDA model structures persuasive communication         ║
║      for behavior change                                    ║
║  📊  Data-driven analysis enables continuous improvement    ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 📚 Conclusion

This lab demonstrated practical **audience segmentation** for cybersecurity training programs. You implemented Python-based segmentation using multiple criteria — role, location, risk factors — and applied the **AIDA model** to create targeted, personalized training messages.

These techniques apply broadly to:

- 🛡️ Security awareness programs
- 📋 Compliance training
- 🏢 Organizational communication strategies

The segmentation approach scales to larger organizations and can incorporate additional factors like compliance status, geographic regulations, or business unit requirements.

---

<div align="center">

![Python](https://img.shields.io/badge/Built%20with-Python%203-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AIDA](https://img.shields.io/badge/Model-AIDA-blueviolet?style=for-the-badge)
![Al Nafi](https://img.shields.io/badge/Lab-Al%20Nafi-orange?style=for-the-badge)

*Happy Learning! 🚀*

</div>
