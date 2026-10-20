🏥 Healthcare Intelligence Dashboard

An interactive, dark-themed healthcare analytics web application built with Streamlit, Plotly, and Pandas. The dashboard provides real-time insights into patient demographics, admission metrics, and hospital financial performance.

🌟 Key Features

Executive KPI Metrics: Real-time tracking of total billing, total admissions, average billing per admission, and average length of stay (ALOS) with period-over-period delta comparisons.

Dynamic Multi-Level Filtering:

Admission date range selector with automatic prior-period benchmarking.

Multi-select filters for Medical Conditions, Admission Types, Insurance Providers, Gender, and Age Groups.

Patient Intelligence:

Demographics breakdown (Age Group distribution, Gender ratio, and Condition prevalence).

Blood type percentage distribution charts.

Emergency admission rate and unique patient counts.

Financial Intelligence:

Revenue breakdown by medical condition.

Revenue distribution across insurance providers.

Comprehensive revenue statistics (Total, Average, Min, and Max billing amounts).

Interactive Raw Data Explorer: Filtered table view with sortable columns and record count indicators.

Modern Cyberpunk UI: Custom glassmorphism dark theme with animated radial gradients, responsive metric cards, and custom scrollbars.

🛠️ Tech Stack & Dependencies

Language: Python 3.9+

Web Framework: Streamlit

Data Manipulation: Pandas

Data Visualizations: Plotly Express

Excel Parser: openpyxl

📂 Project Structure

healthcare-dashboard/
│
├── healthcare_dashboard.py   # Main Streamlit dashboard application
├── Healthcare report.xlsx    # Sample healthcare dataset
├── requirements.txt          # Python package dependencies
└── README.md                 # Project documentation and setup guide


🚀 Local Setup & Installation

1. Clone the Repository

git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>


2. Create and Activate a Virtual Environment (Optional but Recommended)

Windows:

python -m venv venv
.\venv\Scripts\activate


macOS / Linux:

python3 -m venv venv
source venv/bin/activate


3. Install Dependencies

pip install -r requirements.txt


4. Run the Streamlit Application

streamlit run healthcare_dashboard.py


The app will open automatically in your browser at http://localhost:8501.

📊 Dataset Schema

The dashboard expects an Excel spreadsheet (Healthcare report.xlsx) containing the following primary columns:

Column Name

Type

Description

Name

String

Patient full name

Age

Numeric

Age in years

Gender

String

Patient gender (Male, Female, etc.)

Blood Type

String

Patient blood group (A+, O-, etc.)

Medical Condition

String

Diagnosed primary condition

Date of Admission

Date

Admission date (DD-MM-YYYY)

Discharge Date

Date

Discharge date (DD-MM-YYYY)

Admission Type

String

Category (Emergency, Elective, Urgent)

Insurance Provider

String

Health insurance company name

Billing Amount

Numeric

Total hospital charges per admission

🌐 Deployment (Streamlit Community Cloud)

Fork or push this repository to GitHub.

Sign in to Streamlit Community Cloud with your GitHub account.

Click New app, select this repository, set the branch to main, and enter healthcare_dashboard.py as the main file path.

Click Deploy!

📄 License & Attribution

This project is open-source and intended for analytical and educational use. Sample datasets contain mock, de-identified patient data compliant with healthcare privacy guidelines.
