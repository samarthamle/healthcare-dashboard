# 🏥 Healthcare Intelligence Dashboard

An interactive, dark-themed healthcare analytics web application built with **Streamlit**, **Plotly**, and **Pandas**. The dashboard provides real-time insights into patient demographics, admission metrics, and hospital financial performance.

---

## 🌟 Key Features

* **Executive KPI Metrics:** Real-time tracking of total billing, total admissions, average billing per admission, and average length of stay (ALOS) with period-over-period delta comparisons.
* **Dynamic Multi-Level Filtering:**
  * Admission date range selector with automatic prior-period benchmarking.
  * Multi-select filters for Medical Conditions, Admission Types, Insurance Providers, Gender, and Age Groups.
* **Patient Intelligence:**
  * Demographics breakdown (Age Group distribution, Gender ratio, and Condition prevalence).
  * Blood type percentage distribution charts.
  * Emergency admission rate and unique patient counts.
* **Financial Intelligence:**
  * Revenue breakdown by medical condition.
  * Revenue distribution across insurance providers.
  * Comprehensive revenue statistics (Total, Average, Min, and Max billing amounts).
* **Interactive Raw Data Explorer:** Filtered table view with sortable columns and record count indicators.
* **Modern Cyberpunk UI:** Custom glassmorphism dark theme with animated radial gradients, responsive metric cards, and custom scrollbars.

---

## 🛠 Tech Stack & Dependencies

* **Language:** Python 3.9+
* **Web Framework:** [Streamlit](https://streamlit.io/)
* **Data Manipulation:** [Pandas](https://pandas.pydata.org/)
* **Data Visualizations:** [Plotly Express](https://plotly.com/python/)
* **Excel Engine:** [openpyxl](https://openpyxl.readthedocs.io/)

---

## 📁 Project Structure

```text
healthcare-dashboard/
├── healthcare_dashboard.py   # Main Streamlit dashboard application
├── Healthcare report.xlsx    # Sample healthcare dataset
├── requirements.txt          # Python package dependencies
└── README.md                 # Project documentation and setup guide
```

---

## 🚀 Local Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/samarthamle/healthcare-dashboard.git
cd healthcare-dashboard
```

### 2. Create and Activate a Virtual Environment

* **Windows:**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```
* **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application
```bash
streamlit run healthcare_dashboard.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 📊 Dataset Schema

The dashboard expects an Excel spreadsheet (`Healthcare report.xlsx`) containing the following columns:

| Column Name | Expected Format | Description |
| :--- | :--- | :--- |
| `Name` | String | Patient full name |
| `Age` | Integer | Patient age in years |
| `Gender` | String | Gender category |
| `Blood Type` | String | ABO/Rh blood group |
| `Medical Condition` | String | Primary diagnosed medical condition |
| `Date of Admission` | Date (`DD-MM-YYYY`) | Hospital admission date |
| `Discharge Date` | Date (`DD-MM-YYYY`) | Hospital discharge date |
| `Admission Type` | String | `Emergency`, `Elective`, or `Urgent` |
| `Insurance Provider`| String | Associated health insurer |
| `Billing Amount` | Numeric / Float | Total billed cost |