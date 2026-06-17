# 📊 Data-Driven Behavior Change

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![D3.js](https://img.shields.io/badge/D3.js-F9A03C?style=for-the-badge&logo=d3dotjs&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![CSV](https://img.shields.io/badge/CSV-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

![License](https://img.shields.io/badge/License-Educational-blue?style=flat-square)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Dashboard](https://img.shields.io/badge/Feature-Interactive%20Dashboard-blueviolet?style=flat-square)

> *Design behavior tracking systems, analyze security metrics with Python, and build interactive D3.js dashboards to drive measurable cybersecurity culture change.*

</div>

---

## 📋 Table of Contents

- [🎯 Objectives](#-objectives)
- [✅ Prerequisites](#-prerequisites)
- [🖥️ Lab Environment](#️-lab-environment)
- [🏗️ Task 1 — Behavior Tracking Infrastructure](#️-task-1-set-up-behavior-tracking-infrastructure)
- [🔬 Task 2 — Behavior Analysis](#-task-2-implement-behavior-analysis)
- [📈 Task 3 — Interactive Dashboard](#-task-3-build-interactive-dashboard)
- [🧠 Task 4 — Insights & Recommendations](#-task-4-generate-insights-and-recommendations)
- [🏆 Expected Outcomes](#-expected-outcomes)
- [🐛 Troubleshooting](#-troubleshooting-tips)
- [📌 Key Takeaways](#-key-takeaways)

---

## 🎯 Objectives

By the end of this lab, students will be able to:

- 🛠️ Design and implement **behavior tracking systems** for cybersecurity awareness programs
- 📊 Analyze behavior change data using **Python and statistical methods**
- 📉 Create **interactive visualizations** to communicate security metrics
- 🔍 Identify **patterns and trends** in employee security behavior
- 💡 Generate **actionable recommendations** for improving security culture

---

## ✅ Prerequisites

Before starting this lab, students should have:

| Requirement | Details |
|---|---|
| 🐍 Python | Basic knowledge of pandas and matplotlib |
| 🔐 Cybersecurity | Understanding of security awareness concepts |
| 🌐 Web Technologies | Familiarity with HTML, CSS, and JavaScript basics |
| 🐧 Linux | Access to a Linux terminal environment |

---

## 🖥️ Lab Environment

> **Al Nafi** provides ready-to-use Linux-based cloud machines for this lab.
> Simply click **Start Lab** to access your pre-configured environment with **Python 3**, **Node.js**, and required libraries pre-installed.

---

## 🏗️ Task 1: Set Up Behavior Tracking Infrastructure

### 📁 Step 1 — Create Project Structure

Create the necessary directories and install dependencies:

```bash
# Create project structure
mkdir -p ~/behavior-lab/{data,scripts,visualizations,web}
cd ~/behavior-lab

# Install required packages
sudo apt update
sudo apt install -y python3-pip nodejs npm
pip3 install pandas numpy matplotlib seaborn
```

### 📄 Step 2 — Create Behavior Tracking Template

Generate a CSV template for tracking employee security behaviors:

```bash
cat > data/behavior_template.csv << 'EOF'
Employee_ID,Department,Training_Date,Pre_Score,Post_Score,Phishing_Test_1,Phishing_Test_2,Phishing_Test_3,Password_Compliance,MFA_Enabled,Incident_Reports,Behavior_Score,Risk_Level
EMP001,IT,2024-01-15,35,82,Failed,Passed,Passed,Yes,Yes,1,7.5,Low
EMP002,HR,2024-01-15,28,88,Failed,Failed,Passed,Yes,Yes,0,8.2,Low
EMP003,Finance,2024-01-16,42,68,Passed,Passed,Passed,No,No,2,5.8,Medium
EMP004,Marketing,2024-01-16,18,92,Failed,Passed,Passed,Yes,Yes,0,8.9,Low
EMP005,Operations,2024-01-17,38,52,Failed,Failed,Failed,No,No,4,3.1,High
EOF
```

### 🐍 Step 3 — Create Data Generation Script

Create a Python script to generate sample behavior data:

```bash
cat > scripts/generate_data.py << 'EOF'
#!/usr/bin/env python3
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_behavior_data(num_employees=50):
    """
    Generate sample behavior change data for analysis.

    Args:
        num_employees: Number of employee records to generate

    Returns:
        DataFrame with behavior tracking data
    """
    # TODO: Define departments and roles lists
    # TODO: Generate employee records with random data
    # TODO: Calculate behavior scores based on metrics
    # TODO: Assign risk levels (Low/Medium/High)
    # TODO: Return pandas DataFrame
    pass

def calculate_behavior_score(metrics):
    """
    Calculate overall behavior score from individual metrics.

    Args:
        metrics: Dictionary containing behavior metrics

    Returns:
        Float score between 0-10
    """
    # TODO: Weight knowledge improvement (20%)
    # TODO: Weight phishing test performance (30%)
    # TODO: Weight policy compliance (25%)
    # TODO: Weight incident reporting (15%)
    # TODO: Weight tool usage (10%)
    # TODO: Return weighted total score
    pass

if __name__ == "__main__":
    df = generate_behavior_data(50)
    df.to_csv('../data/behavior_data.csv', index=False)
    print(f"Generated {len(df)} employee records")
EOF

chmod +x scripts/generate_data.py
```

---

## 🔬 Task 2: Implement Behavior Analysis

### 🧮 Step 1 — Create Analysis Script

Build a comprehensive analysis tool:

```bash
cat > scripts/analyze_behavior.py << 'EOF'
#!/usr/bin/env python3
import pandas as pd
import numpy as np
import json

class BehaviorAnalyzer:
    def __init__(self, data_file):
        """Initialize analyzer with behavior data."""
        self.df = pd.read_csv(data_file)
        self.df['Training_Date'] = pd.to_datetime(self.df['Training_Date'])

    def calculate_summary_statistics(self):
        """
        Calculate key summary statistics.

        Returns:
            Dictionary with summary metrics
        """
        # TODO: Calculate total employees analyzed
        # TODO: Calculate average pre/post training scores
        # TODO: Calculate knowledge improvement metrics
        # TODO: Calculate average behavior score
        # TODO: Return dictionary with all statistics
        pass

    def analyze_by_department(self):
        """
        Analyze behavior metrics grouped by department.

        Returns:
            DataFrame with department-level statistics
        """
        # TODO: Group data by department
        # TODO: Calculate mean scores per department
        # TODO: Calculate knowledge improvement per department
        # TODO: Identify best and worst performing departments
        # TODO: Return aggregated DataFrame
        pass

    def analyze_phishing_performance(self):
        """
        Analyze phishing simulation results over time.

        Returns:
            Dictionary with phishing metrics
        """
        # TODO: Calculate pass rates for each simulation
        # TODO: Calculate improvement from sim 1 to sim 3
        # TODO: Analyze performance by department
        # TODO: Identify employees needing additional training
        # TODO: Return analysis results
        pass

    def assess_risk_levels(self):
        """
        Analyze risk distribution and identify high-risk employees.

        Returns:
            Dictionary with risk assessment data
        """
        # TODO: Calculate risk level distribution
        # TODO: Identify high-risk employees
        # TODO: Analyze risk factors by department
        # TODO: Calculate percentage in each risk category
        # TODO: Return risk assessment results
        pass

    def generate_recommendations(self):
        """
        Generate actionable recommendations based on analysis.

        Returns:
            List of recommendation strings
        """
        # TODO: Analyze knowledge improvement trends
        # TODO: Evaluate phishing test performance
        # TODO: Check policy compliance rates
        # TODO: Identify departments needing attention
        # TODO: Return list of specific recommendations
        pass

    def export_results(self, output_file):
        """
        Export analysis results to JSON for visualization.

        Args:
            output_file: Path to output JSON file
        """
        # TODO: Compile all analysis results
        # TODO: Format data for D3.js consumption
        # TODO: Write to JSON file
        # TODO: Print confirmation message
        pass

def main():
    analyzer = BehaviorAnalyzer('../data/behavior_data.csv')

    # TODO: Run all analysis methods
    # TODO: Print formatted report
    # TODO: Export results for visualization
    # TODO: Generate timestamp
    pass

if __name__ == "__main__":
    main()
EOF

chmod +x scripts/analyze_behavior.py
```

### 📉 Step 2 — Create Visualization Generator

Build static visualization generator:

```bash
cat > scripts/create_charts.py << 'EOF'
#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class VisualizationGenerator:
    def __init__(self, data_file):
        """Initialize with behavior data."""
        self.df = pd.read_csv(data_file)
        plt.style.use('seaborn-v0_8')

    def create_knowledge_improvement_chart(self):
        """
        Create before/after training comparison chart.

        Saves: knowledge_improvement.png
        """
        # TODO: Create figure with 2 subplots
        # TODO: Plot pre-training score distribution
        # TODO: Plot post-training score distribution
        # TODO: Add labels, title, and legend
        # TODO: Save to visualizations directory
        pass

    def create_behavior_score_dashboard(self):
        """
        Create comprehensive behavior score dashboard.

        Saves: behavior_dashboard.png
        """
        # TODO: Create 2x2 subplot grid
        # TODO: Plot overall score distribution
        # TODO: Plot scores by department
        # TODO: Plot risk level pie chart
        # TODO: Plot score vs improvement scatter
        # TODO: Save dashboard image
        pass

    def create_phishing_progression_chart(self):
        """
        Create phishing test progression visualization.

        Saves: phishing_progression.png
        """
        # TODO: Calculate pass rates for each simulation
        # TODO: Create line chart showing progression
        # TODO: Add department comparison bars
        # TODO: Annotate with percentages
        # TODO: Save chart image
        pass

    def create_compliance_heatmap(self):
        """
        Create policy compliance heatmap by department.

        Saves: compliance_heatmap.png
        """
        # TODO: Aggregate compliance metrics by department
        # TODO: Create heatmap with seaborn
        # TODO: Add color scale and annotations
        # TODO: Format labels and title
        # TODO: Save heatmap image
        pass

def main():
    generator = VisualizationGenerator('../data/behavior_data.csv')

    # TODO: Generate all visualizations
    # TODO: Print confirmation messages
    pass

if __name__ == "__main__":
    main()
EOF

chmod +x scripts/create_charts.py
```

---

## 📈 Task 3: Build Interactive Dashboard

### 🌐 Step 1 — Create HTML Dashboard Structure

Build the web interface:

```bash
cat > web/dashboard.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Behavior Change Dashboard</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .dashboard {
            max-width: 1400px;
            margin: 0 auto;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        .metric-card {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .chart-container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        /* TODO: Add more styles for charts and interactive elements */
    </style>
</head>
<body>
    <div class="dashboard">
        <div class="header">
            <h1>Cybersecurity Behavior Change Dashboard</h1>
            <p>Real-time analysis of security awareness metrics</p>
        </div>

        <div class="metrics-grid" id="metrics">
            <!-- TODO: Metric cards will be populated by JavaScript -->
        </div>

        <div class="chart-container">
            <h2>Knowledge Improvement Analysis</h2>
            <div id="knowledge-chart"></div>
        </div>

        <div class="chart-container">
            <h2>Department Performance</h2>
            <div id="department-chart"></div>
        </div>

        <div class="chart-container">
            <h2>Risk Distribution</h2>
            <div id="risk-chart"></div>
        </div>
    </div>

    <script src="dashboard.js"></script>
</body>
</html>
EOF
```

### ⚡ Step 2 — Create Dashboard JavaScript

Implement interactive visualizations:

```bash
cat > web/dashboard.js << 'EOF'
// Load and process behavior data
async function loadData() {
    // TODO: Fetch data from JSON file
    // TODO: Parse and validate data
    // TODO: Return processed data object
}

// Create metric cards
function createMetricCards(data) {
    // TODO: Calculate key metrics
    // TODO: Create card elements
    // TODO: Populate with data
    // TODO: Append to metrics grid
}

// Create knowledge improvement chart
function createKnowledgeChart(data) {
    // TODO: Set up SVG dimensions
    // TODO: Create scales for x and y axes
    // TODO: Draw bars for pre/post training scores
    // TODO: Add axes and labels
    // TODO: Add interactive tooltips
}

// Create department performance chart
function createDepartmentChart(data) {
    // TODO: Aggregate data by department
    // TODO: Create horizontal bar chart
    // TODO: Color code by performance level
    // TODO: Add value labels
    // TODO: Implement hover effects
}

// Create risk distribution pie chart
function createRiskChart(data) {
    // TODO: Calculate risk level counts
    // TODO: Create pie chart with D3
    // TODO: Add color coding (green/yellow/red)
    // TODO: Add percentage labels
    // TODO: Implement click interactions
}

// Create phishing progression line chart
function createPhishingChart(data) {
    // TODO: Extract phishing test results
    // TODO: Create line chart showing progression
    // TODO: Add data points and labels
    // TODO: Implement zoom functionality
}

// Initialize dashboard
async function initDashboard() {
    // TODO: Load data
    // TODO: Create all visualizations
    // TODO: Set up event listeners
    // TODO: Implement auto-refresh
}

// Run initialization when page loads
document.addEventListener('DOMContentLoaded', initDashboard);
EOF
```

### 📤 Step 3 — Create Data Export Script

Generate JSON data for the dashboard:

```bash
cat > scripts/export_for_web.py << 'EOF'
#!/usr/bin/env python3
import pandas as pd
import json

def export_dashboard_data(input_file, output_file):
    """
    Export behavior data in format suitable for web dashboard.

    Args:
        input_file:  Path to CSV data file
        output_file: Path to output JSON file
    """
    # TODO: Load CSV data
    # TODO: Calculate summary statistics
    # TODO: Aggregate by department
    # TODO: Format for D3.js consumption
    # TODO: Write to JSON file
    pass

if __name__ == "__main__":
    export_dashboard_data(
        '../data/behavior_data.csv',
        '../web/dashboard_data.json'
    )
EOF

chmod +x scripts/export_for_web.py
```

---

## 🧠 Task 4: Generate Insights and Recommendations

### 🔍 Step 1 — Implement Pattern Detection

Create advanced analysis for identifying trends:

```bash
cat > scripts/detect_patterns.py << 'EOF'
#!/usr/bin/env python3
import pandas as pd
import numpy as np

class PatternDetector:
    def __init__(self, data_file):
        """Initialize pattern detector with behavior data."""
        self.df = pd.read_csv(data_file)

    def identify_improvement_trends(self):
        """
        Identify employees showing consistent improvement.

        Returns:
            List of employee IDs with positive trends
        """
        # TODO: Calculate improvement metrics
        # TODO: Identify consistent improvers
        # TODO: Flag employees needing attention
        # TODO: Return analysis results
        pass

    def detect_risk_factors(self):
        """
        Identify common factors among high-risk employees.

        Returns:
            Dictionary of risk factor correlations
        """
        # TODO: Analyze high-risk employee characteristics
        # TODO: Calculate correlation with risk level
        # TODO: Identify common patterns
        # TODO: Return risk factor analysis
        pass

    def predict_future_performance(self):
        """
        Predict future behavior scores based on current trends.

        Returns:
            DataFrame with predictions
        """
        # TODO: Calculate trend lines
        # TODO: Project future scores
        # TODO: Identify at-risk employees
        # TODO: Return predictions
        pass

    def generate_intervention_recommendations(self):
        """
        Generate targeted intervention recommendations.

        Returns:
            Dictionary mapping employees to recommended actions
        """
        # TODO: Analyze individual performance
        # TODO: Match to intervention strategies
        # TODO: Prioritize by risk level
        # TODO: Return recommendation mapping
        pass

def main():
    detector = PatternDetector('../data/behavior_data.csv')

    # TODO: Run all pattern detection methods
    # TODO: Generate comprehensive report
    # TODO: Export recommendations
    pass

if __name__ == "__main__":
    main()
EOF

chmod +x scripts/detect_patterns.py
```

### ▶️ Step 2 — Test the Complete System

Run all components:

```bash
# Generate sample data
cd ~/behavior-lab/scripts
python3 generate_data.py

# Run analysis
python3 analyze_behavior.py

# Create visualizations
python3 create_charts.py

# Export for web dashboard
python3 export_for_web.py

# Start web server
cd ../web
python3 -m http.server 8080
```

Access the dashboard at:

```
http://localhost:8080/dashboard.html
```

---

## 🏆 Expected Outcomes

After completing this lab, you should have:

| ✅ Deliverable | Description |
|---|---|
| 📄 Tracking System | Functional behavior tracking system with CSV templates |
| 🐍 Analysis Scripts | Python scripts that analyze security awareness metrics |
| 📉 Visualizations | Static visualizations showing key trends and patterns |
| 🌐 Web Dashboard | Interactive web dashboard displaying real-time metrics |
| 💡 Recommendations | Automated recommendation generation based on data analysis |
| 🧠 Understanding | Knowledge of how to measure behavior change effectiveness |

---

## 🐛 Troubleshooting Tips

### ⚠️ Issue: Import Errors for Pandas or Matplotlib

> **Solution:** Ensure all packages are installed.

```bash
pip3 install pandas numpy matplotlib seaborn
```

### ⚠️ Issue: D3.js Charts Not Rendering

> **Solution:** Check browser console for errors and verify JSON data format.

```bash
# Verify JSON file was generated correctly
cat web/dashboard_data.json | python3 -m json.tool

# Ensure D3.js CDN is accessible
# Check browser developer console for specific errors
```

### ⚠️ Issue: Empty or Incorrect Analysis Results

> **Solution:** Verify CSV file format matches template.

```bash
# Check your CSV structure
head -n 5 data/behavior_data.csv

# Ensure date format is correct (YYYY-MM-DD)
# Check for missing values in key columns
```

### ⚠️ Issue: Web Server Not Accessible

> **Solution:** Check firewall settings and port availability.

```bash
# Check if port 8080 is already in use
lsof -i :8080

# Try an alternative port
python3 -m http.server 8081
```

---

## 📌 Key Takeaways

```
╔══════════════════════════════════════════════════════════════╗
║                     KEY TAKEAWAYS                           ║
╠══════════════════════════════════════════════════════════════╣
║  📊  Behavior change requires systematic tracking           ║
║  🔍  Data analysis reveals patterns not visible through     ║
║      observation alone                                      ║
║  📉  Visualizations make complex metrics accessible         ║
║      to stakeholders                                        ║
║  🔄  Continuous monitoring enables proactive intervention   ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 📚 Conclusion

This lab demonstrated how to implement a comprehensive **data-driven approach** to measuring and improving cybersecurity behavior. You created:

- 🛠️ **Tracking systems** with CSV templates
- 📊 **Statistical analysis** with Python and pandas
- 📉 **Visualizations** using matplotlib, seaborn, and D3.js
- 🌐 **An interactive dashboard** for real-time metric display

These skills are essential for security awareness professionals who need to demonstrate program effectiveness and make **data-informed decisions** about security culture initiatives.

Apply these techniques to real-world security awareness programs to improve organizational security posture through **measurable behavior change**.

---

<div align="center">

![Python](https://img.shields.io/badge/Built%20with-Python%203-3776AB?style=for-the-badge&logo=python&logoColor=white)
![D3.js](https://img.shields.io/badge/Visualized%20with-D3.js-F9A03C?style=for-the-badge&logo=d3dotjs&logoColor=black)
![Al Nafi](https://img.shields.io/badge/Lab-Al%20Nafi-orange?style=for-the-badge)

*Happy Learning! 🚀*

</div>
