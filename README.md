<div align="center">

#  InsightOS

### AI-Powered Decision Intelligence Platform for Data Quality Assessment

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
![Render](https://img.shields.io/badge/Deployment-Render-46E3B7?logo=render)
![License](https://img.shields.io/badge/License-Academic-green)

*A Flask-based Decision Intelligence Platform that transforms raw datasets into actionable business insights through automated data profiling, quality assessment, and intelligent recommendations.*

</div>

---

#  Overview

InsightOS is an intelligent data engineering platform that automates dataset analysis and metadata extraction. It helps users understand the quality, completeness, and business readiness of uploaded datasets through multiple analytical engines.

Instead of manually inspecting CSV files, users simply upload a dataset and receive:

- Dataset quality assessment
- Metadata extraction
- Data profiling
- Dormant data detection
- Business gap analysis
- AI-inspired decision recommendations
- Downloadable PDF reports

---

#  Key Features

| Feature | Description |
|----------|-------------|
|  CSV Upload | Upload datasets securely through the web interface |
|  Dashboard | Interactive dashboard displaying dataset insights |
|  Data Discovery | Automatic profiling of every dataset column |
|  Quality Score | Calculates overall dataset health |
|  Dormant Detection | Identifies low-value and unused columns |
|  Gap Detection | Detects missing business attributes |
|  Decision Intelligence | Generates actionable recommendations |
|  Metadata Catalog | Maintains history of uploaded datasets |
|  PDF Reports | Export professional dataset reports |
|  SQLite Storage | Stores processed metadata locally |
|  Error Handling | Handles invalid uploads gracefully |

---

#  System Architecture

```text
                        User

                          │
                          ▼

                  Flask Web Application

                          │
      ┌───────────────────┼───────────────────┐
      │                   │                   │
      ▼                   ▼                   ▼

 ETL Pipeline      Discovery Engine   Decision Engine

      │                   │                   │
      └───────────────────┼───────────────────┘
                          ▼

               Processed Dataset Metadata

                          │
                ┌─────────┴─────────┐
                ▼                   ▼

         SQLite Database      PDF Generator

                │
                ▼

        Interactive Dashboard
```

---

#  Technology Stack

## Backend

- Python
- Flask
- Pandas
- SQLite

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Reporting

- ReportLab

## Deployment

- Render

## Version Control

- Git
- GitHub

---

#  Project Structure

```text
InsightOS/

├── app.py
├── config.py
├── etl.py
├── requirements.txt
│
├── database/
│   ├── db.py
│   ├── repository.py
│   └── init_db.py
│
├── engines/
│   ├── discovery.py
│   ├── dormant.py
│   ├── gap.py
│   └── decision.py
│
├── catalog/
│   └── catalog.py
│
├── reports/
│   └── generator.py
│
├── templates/
├── static/
├── uploads/
└── insightos.db
```

---

#  Application Workflow

```text
CSV Upload

      │

      ▼

ETL Pipeline

      │

      ▼

Metadata Extraction

      │

      ▼

Discovery Engine

      │

      ▼

Dormant Detection

      │

      ▼

Gap Detection

      │

      ▼

Decision Intelligence

      │

      ▼

SQLite Storage

      │

      ▼

Dashboard + PDF Report
```

---

#  Analytical Engines

<details>

<summary><strong>🔍 Data Discovery Engine</strong></summary>

Automatically analyzes every column to determine:

- Data type
- Missing values
- Completeness
- Unique values
- Column classification

</details>

<details>

<summary><strong>💤 Dormant Data Detection</strong></summary>

Detects:

- Mostly empty columns
- Constant-value columns
- Low-information attributes

</details>

<details>

<summary><strong>🎯 Gap Detection Engine</strong></summary>

Identifies missing business attributes based on dataset type and recommends improvements.

</details>

<details>

<summary><strong>🧠 Decision Intelligence Engine</strong></summary>

Generates:

- Dataset Health Score
- Overall Health Status
- Intelligent Recommendations

</details>

---

#  PDF Report

InsightOS automatically generates a professional report containing:

- Dataset Summary
- Quality Score
- Missing Values
- Duplicate Records
- Discovery Results
- Dormant Data
- Gap Detection
- Decision Recommendations

---

# Database

SQLite stores:

- Dataset Metadata
- Quality Scores
- Upload History
- Metadata Catalog

---

#  Installation

Clone the repository

```bash
git clone https://github.com/b23in004-maker/InsightOS.git
```

Navigate to the project

```bash
cd InsightOS
```

Create a virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Initialize SQLite

```bash
python database/init_db.py
```

Run

```bash
python app.py
```

Visit

```
http://127.0.0.1:5000
```

---

# 🌐 Deployment

The project is deployed using **Render**.

The application uses SQLite for metadata storage, enabling straightforward deployment without requiring an external database server.

> **Power BI Integration Note**

> Processed metadata is stored in SQLite and structured for future integration with Business Intelligence platforms such as Power BI. During development, Power BI integration was explored conceptually, while visualization was demonstrated directly within the InsightOS dashboard due to local connector compatibility limitations.

---


#  Future Enhancements

-  User Authentication
-  Cloud Database Support
-  Native Power BI Integration
-  Machine Learning Recommendations
-  Predictive Analytics
-  REST API
-  Multiple File Formats
-  Role-Based Access Control
-  Responsive Mobile Dashboard

---

# Author

**Pratheeka Reddy**

Data Engineering Project

Kakatiya Institute of Technology & Science

---

#  Support

If you found this project useful, consider giving it a ⭐ on GitHub!

---

<div align="center">

### Thank you for visiting InsightOS!

</div>
