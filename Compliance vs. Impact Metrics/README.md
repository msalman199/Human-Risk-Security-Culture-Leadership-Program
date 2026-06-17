# Compliance vs. Impact Metrics – Security Culture 

## 📌 Project Purpose

This project is a hands-on cybersecurity analytics lab designed to help learners understand the **difference between compliance metrics and impact metrics** in security awareness and culture programs.

The main goal is to move beyond simple checkbox-based security tracking and develop the ability to measure **real behavioral change** inside an organization using Python-based data analysis.

---

## 🎯 Objectives

By completing this project, you will be able to:

- Differentiate between **compliance metrics** and **impact metrics**
- Build Python tools to collect and analyze security culture data
- Generate datasets for compliance and behavioral analysis
- Perform statistical and trend analysis using pandas and numpy
- Create visual dashboards using matplotlib and seaborn
- Interpret results to improve security awareness programs
- Make data-driven decisions for security culture improvement

---

## 🧠 Key Concepts

### 🔐 Compliance Metrics
Measures whether security rules and training requirements are being followed.

**Examples:**
- Training completion rates
- Policy acknowledgment rates
- Phishing simulation click rates
- Assessment scores

👉 Focus: *"Did people complete required security tasks?"*

---

### 🌱 Impact Metrics
Measures behavioral change and cultural improvement over time.

**Examples:**
- Voluntary incident reporting
- Proactive security behavior
- Peer-to-peer security coaching
- Reduction in security incidents

👉 Focus: *"Did security behavior actually improve?"*

---

## 🛠️ Lab Environment

Your environment includes:

- Python 3.x
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`
- Preconfigured Linux terminal
- Sample dataset generator scripts
- Visualization tools

Install missing dependencies if needed:

```bash
pip3 install pandas numpy matplotlib seaborn
📂 Project Structure
metrics_lab/
│
├── metric_definitions.py
├── data_generator.py
│
├── compliance_analyzer.py
├── compliance_visualizer.py
│
├── impact_analyzer.py
├── impact_visualizer.py
│
├── integrated_dashboard.py
│
├── compliance_metrics.csv   (generated)
├── impact_metrics.csv       (generated)
│
└── *.png (generated charts)
⚙️ Setup Instructions
1. Create Project Directory
mkdir ~/metrics_lab && cd ~/metrics_lab
2. Generate Sample Data
python3 data_generator.py

This will create:

compliance_metrics.csv
impact_metrics.csv
📊 What You Will Build
1. Compliance Analysis System
Department performance comparison
Training and policy adherence tracking
Compliance trend analysis
Gap detection system
2. Impact Analysis System
Behavioral change tracking
Culture maturity scoring
Proactive security behavior analysis
Incident reduction correlation
3. Visualization Dashboard
Trend charts over time
Department comparison graphs
Correlation heatmaps
Behavioral evolution charts
4. Integrated Security Dashboard
Correlation between compliance and impact
Program effectiveness measurement
Executive-level reporting
Strategic recommendations engine
📈 Expected Outputs

After running the full lab, you will generate:

📄 Two structured datasets (CSV files)
📊 Multiple analytical reports
📉 Trend and correlation graphs
🧠 Security culture insights
📌 Executive recommendations
🔍 Key Insights You Will Learn
Compliance ≠ Security Culture
High training completion does not guarantee safe behavior
Impact metrics reflect real organizational change
Combining both metrics gives a complete security picture
Behavioral change is the ultimate goal of security awareness
🚀 How to Run the Project

Run modules in this order:

python3 data_generator.py

python3 compliance_analyzer.py
python3 compliance_visualizer.py

python3 impact_analyzer.py
python3 impact_visualizer.py

python3 integrated_dashboard.py
📌 Troubleshooting
❌ Missing CSV files

Run:

python3 data_generator.py
❌ Missing libraries
pip3 install pandas numpy matplotlib seaborn
❌ Charts not showing

Ensure you use:

plt.savefig("file.png")
🧭 Conclusion

This project demonstrates how modern security programs must go beyond compliance tracking and focus on real human behavior change.

✔ Key Takeaways:
Compliance metrics show activity
Impact metrics show transformation
Both are required for full visibility
Data-driven security culture is measurable and improvable
🔮 Future Improvements
Add real-time log ingestion
Connect to SIEM data sources
Build web-based dashboard (Flask/Dash)
Integrate ML-based behavior prediction
Automate monthly reporting pipelines
👨‍💻 Author

Security Analytics Lab Project – Educational Cybersecurity Program

📜 License

For educational and academic use only.
