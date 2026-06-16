# 🧠 Behavioral Science in Cybersecurity

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Linux](https://img.shields.io/badge/Linux-Ubuntu%20%7C%20Debian-orange?style=for-the-badge&logo=linux)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Behavioral%20Risk-red?style=for-the-badge)
![Behavioral Science](https://img.shields.io/badge/Behavioral%20Science-Fogg%20Model-green?style=for-the-badge)
![Risk Assessment](https://img.shields.io/badge/Risk-Prioritization-purple?style=for-the-badge)

---

# 📖 Introduction

Human behavior remains one of the most significant factors influencing cybersecurity outcomes. Technical controls alone cannot eliminate security risks if users lack the motivation, ability, or triggers required to perform secure behaviors.

This lab introduces the **B.J. Fogg Behavior Model (B = MAT)** and demonstrates how behavioral science principles can be integrated into cybersecurity risk assessment and prioritization. Students will build practical Python tools that evaluate security behaviors, prioritize risks, and generate actionable recommendations for improving organizational security culture.

---

# 🎯 Objectives

By the end of this lab, students will be able to:

- Understand and apply the B.J. Fogg Behavior Model (Motivation, Ability, Trigger) to cybersecurity contexts
- Implement behavioral assessment algorithms in Python
- Develop risk prioritization systems incorporating behavioral science principles
- Analyze security behaviors and generate actionable recommendations
- Create tools for improving organizational security culture

---

# 📋 Prerequisites

Before starting this lab, students should have:

- Basic Python programming (functions, classes, dictionaries, lists)
- Understanding of Linux command line operations
- Familiarity with cybersecurity concepts (threats, vulnerabilities, risk)
- Basic knowledge of human behavior and motivation concepts

---

# ☁️ Lab Environment Setup

Al Nafi provides pre-configured Linux-based cloud machines.

### Environment Includes

- Python 3.8+
- Nano and Vim editors
- Linux terminal environment
- Standard Python libraries
- Pre-installed dependencies

---

# 🧩 Understanding the B.J. Fogg Model

The B.J. Fogg Behavior Model states:

> **B = MAT**

Behavior occurs when:

- **Motivation** → Desire to perform the behavior
- **Ability** → Capacity to perform the behavior
- **Trigger** → Prompt initiating the behavior

Each component is measured on a scale of:

```text
0 = Very Low
10 = Very High
```

---

# 🚀 Task 1: Implement the B.J. Fogg Behavior Model

## 🔹 Step 1: Create Project Directory

```bash
mkdir ~/fogg_cybersecurity_lab
cd ~/fogg_cybersecurity_lab
```

---

## 🔹 Step 2: Create Fogg Model Implementation

Create:

```bash
nano fogg_model.py
```

### Python Implementation Template

```python
#!/usr/bin/env python3
"""
B.J. Fogg Behavior Model Implementation for Cybersecurity
Students: Complete the TODO sections to implement the model
"""

import json
import datetime
from typing import Dict, List

class FoggBehaviorModel:
    """
    Implementation of B.J. Fogg's Behavior Model for cybersecurity contexts
    """
    
    def __init__(self):
        self.behavior_history = []
    
    def calculate_behavior_score(self, motivation: float, ability: float, trigger: float) -> float:
        """
        Calculate behavior likelihood based on Fogg's B=MAT model
        """

        # TODO:
        # Normalize values
        # Apply formula
        # Return rounded score

        pass
    
    def assess_cybersecurity_behavior(self, behavior_name: str, user_profile: Dict) -> Dict:
        """
        Assess cybersecurity behavior
        """

        # TODO:
        # Extract values
        # Calculate behavior score
        # Determine risk level
        # Generate recommendations

        pass
    
    def _generate_recommendations(self, motivation: float, ability: float, trigger: float) -> List[str]:
        """
        Generate recommendations
        """

        recommendations = []

        # TODO:
        # Motivation recommendations
        # Ability recommendations
        # Trigger recommendations

        return recommendations
    
    def get_behavior_trends(self) -> Dict:
        """
        Analyze trends
        """

        if not self.behavior_history:
            return {"message": "No behavior data available"}

        # TODO

        pass
    
    def export_data(self, filename: str) -> bool:
        """
        Export to JSON
        """

        # TODO

        pass

if __name__ == "__main__":
    fogg = FoggBehaviorModel()

    user1 = {'motivation': 7, 'ability': 4, 'trigger': 8}
    result1 = fogg.assess_cybersecurity_behavior("Password Management", user1)

    print(result1)
```

---

## 🔹 Make Executable

```bash
chmod +x fogg_model.py
```

---

## 🔹 Step 3: Run the Program

```bash
python3 fogg_model.py
```

Expected output:

```text
Behavior Score: XX.XX
Likelihood: Medium
Risk Level: Medium
Recommendations:
- Training
- Better reminders
```

---

# 🚀 Task 2: Develop a Risk Prioritization Algorithm

---

## 🔹 Step 1: Create Risk Prioritization Module

```bash
nano risk_prioritization.py
```

### Starter Code

```python
#!/usr/bin/env python3

import json
from typing import Dict, List
from fogg_model import FoggBehaviorModel

class CybersecurityRiskPrioritizer:

    def __init__(self):
        self.fogg_model = FoggBehaviorModel()
        self.risk_database = []
        self.prioritized_risks = []

    def add_risk_scenario(
        self,
        risk_id,
        risk_name,
        impact_score,
        user_profiles,
        threat_frequency
    ):
        """
        Add risk scenario
        """

        # TODO

        pass

    def calculate_risk_priority_score(self, risk_scenario):
        """
        Formula:
        Priority =
        (Impact × Frequency × Behavioral_Risk_Factor) / 100
        """

        # TODO

        pass

    def prioritize_risks(self):

        self.prioritized_risks = []

        # TODO

        pass

    def _generate_risk_recommendations(self, risk_scenario):

        recommendations = []

        # TODO

        return recommendations

    def generate_risk_report(self):

        # TODO

        pass

    def export_prioritized_risks(self, filename):

        # TODO

        pass
```

---

## 🔹 Run Risk Prioritization

```bash
python3 risk_prioritization.py
```

Expected Output:

```text
Top Priority Risks:

Phishing Email Attacks
Priority Score: 72.5

Unauthorized Software Installation
Priority Score: 31.4
```

---

# 🚀 Task 3: Create Comprehensive Testing Suite

---

## 🔹 Step 1: Create Test File

```bash
nano test_system.py
```

### Starter Code

```python
#!/usr/bin/env python3

from fogg_model import FoggBehaviorModel
from risk_prioritization import CybersecurityRiskPrioritizer

def test_fogg_model():

    print("Testing Fogg Model")

    # TODO

    pass

def test_risk_prioritization():

    print("Testing Prioritization")

    # TODO

    pass

def test_data_export():

    print("Testing Export")

    # TODO

    pass

def run_integration_test():

    print("Running Integration Test")

    # TODO

    pass

if __name__ == "__main__":

    test_fogg_model()
    test_risk_prioritization()
    test_data_export()
    run_integration_test()

    print("All Tests Complete")
```

---

## 🔹 Run Tests

```bash
python3 test_system.py
```

Expected:

```text
PASS - Fogg Score Calculation
PASS - Recommendation Generation
PASS - Risk Prioritization
PASS - Data Export

All Tests Complete
```

---

# 🚀 Task 4: Apply to Real-World Scenario

---

## 🔹 Step 1: Create Organizational Assessment Tool

```bash
nano org_assessment.py
```

### Requirements

Implement a tool that:

- Defines multiple departments
- Assesses security behavior
- Prioritizes risks
- Generates recommendations
- Exports reports

---

## Example Departments

```python
departments = {
    "IT": {
        "motivation": 8,
        "ability": 9,
        "trigger": 7
    },
    "Finance": {
        "motivation": 7,
        "ability": 5,
        "trigger": 6
    },
    "HR": {
        "motivation": 8,
        "ability": 4,
        "trigger": 5
    }
}
```

---

## 🔹 Run Assessment

```bash
python3 org_assessment.py
```

Review:

- Highest-risk departments
- Weakest security behaviors
- Most effective interventions

---

# 🔍 Verification Checklist

Run:

```bash
echo "=== Behavioral Science Verification ==="

ls

python3 fogg_model.py

python3 risk_prioritization.py

python3 test_system.py

python3 org_assessment.py
```

---

# ✅ Expected Outcomes

After completing this lab, students should have:

### 🧠 Functional Fogg Model

- Motivation assessment
- Ability assessment
- Trigger assessment
- Behavioral scoring

### 📊 Risk Prioritization System

- Risk scoring
- Priority ranking
- Recommendation generation

### 🧪 Testing Framework

- Unit tests
- Integration tests
- Validation scenarios

### 🏢 Organizational Assessment Tool

- Department analysis
- Risk profiling
- Security culture evaluation

### 📄 Reports

- JSON exports
- Risk summaries
- Organizational recommendations

---

# 🛠 Troubleshooting

---

## Issue: Behavior Scores Incorrect

Verify normalization:

```python
value = max(0, min(value, 10))
normalized = value / 10
```

Formula:

```python
score = motivation * ability * trigger
```

---

## Issue: Risk Prioritization Incorrect

Verify:

```python
behavioral_risk_factor = 100 - avg_behavior_score
```

Priority Formula:

```python
Priority =
(Impact × Frequency × Behavioral_Risk_Factor) / 100
```

---

## Issue: Empty Recommendations

Check thresholds:

```python
if motivation < 5:
```

```python
if ability < 5:
```

```python
if trigger < 5:
```

---

## Issue: JSON Export Fails

Verify:

```python
try:
    with open(file, "w") as f:
        json.dump(data, f)
except Exception:
    pass
```

---

# 🎓 Key Insights

Behavioral science provides a powerful enhancement to traditional cybersecurity risk assessment.

Important observations:

- Low ability is often a larger risk factor than low motivation
- Effective triggers can significantly improve secure behavior
- Different departments require different interventions
- Behavioral analytics provide actionable security insights

---

# 🌍 Real-World Applications

- Security awareness program design
- Security culture improvement initiatives
- Human risk management
- Compliance assessments
- Insider risk analysis
- Risk-based training programs
- Behavioral security metrics

---

# 📚 Conclusion

In this lab, you successfully explored how the **B.J. Fogg Behavior Model** can be applied to cybersecurity. By implementing behavioral assessment algorithms, risk prioritization systems, and organizational analysis tools, you gained practical experience in combining behavioral science with cybersecurity risk management.

The skills developed in this lab provide a foundation for:

- Human-centered cybersecurity programs
- Security awareness optimization
- Behavioral risk assessment
- Organizational security culture improvement
- Risk-based decision making

Understanding how motivation, ability, and triggers influence security behavior enables organizations to create more effective interventions and significantly improve their overall security posture.

---
⭐ If you found this project useful, consider starring the repository and sharing it with other cybersecurity learners.
