# 🔒 SecurePipe — Lightweight DevSecOps Security Scanner

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Security Scans](https://github.com/Swapnil-Chatterjee/SecurePipe/actions/workflows/securepipe.yml/badge.svg)
![Status](https://img.shields.io/badge/Build-Passing-success)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen)

> 🚀 **SecurePipe** is a lightweight, modular Python-based **DevSecOps security scanner** that integrates  
> **Bandit**, **Checkov**, and (soon) **Trivy** to detect code and configuration vulnerabilities.  
> Designed for **developers and security engineers** who want to automate vulnerability checks in CI/CD pipelines.

---

## 🧩 Features

- 🐍 **Python CLI** — Scan your entire repo with a single command  
- 🕵️ **Bandit Integration** — Detects Python code security issues (SAST)  
- ☁️ **Checkov Integration** — Scans Infrastructure-as-Code (Terraform, Docker, YAML, etc.)  
- 🧱 **Modular Design** — Each scanner runs independently and stores results in JSON format  
- 📊 **Unified Summary** — Aggregated output in Rich tables (HTML/Markdown reports coming soon)  
- ⚙️ **CI/CD Integration** — GitHub Actions workflow runs on push or pull request  
- 🌐 **Future Add-on** — Flask dashboard for viewing scan history and uploading reports  

---

## 📁 Project Structure

```
SecurePipe/
│
├── securepipe.py               # Main CLI script
├── requirements.txt            # Python dependencies
├── demo.tf                     # Sample Terraform file (for Checkov testing)
├── .gitignore
│
├── reports/                    # Generated reports (Bandit / Checkov JSON)
│   ├── bandit_report.json
│   ├── results_json.json
│   └── checkov_console.log
│
├── scanners/                   # (Optional) future modular scanners
│
└── .github/
    └── workflows/
        └── securepipe.yml       # GitHub Actions workflow
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Swapnil-Chatterjee/SecurePipe.git
cd SecurePipe
```

---

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

**Activate:**
- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Scanner

```bash
python securepipe.py --repo ../target_repo
```

Reports will be saved in the `reports/` directory.

---

## 🧪 Example Output

```
🔍 Running Bandit (Python security scan)...
☁️  Running Checkov (IaC / config scan)...

🔒 SecurePipe Scan Summary
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Tool          ┃ Issues Found ┃         Report Path         ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Bandit               │     12       │ reports/bandit_report.json  │
│ Checkov (terraform)  │      4       │ reports/results_json.json   │
│ Checkov (dockerfile) │      1       │ reports/results_json.json   │
└──────────────────────┴──────────────┴─────────────────────────────┘

✅ Scanning complete! Reports saved in ./reports
```

---
