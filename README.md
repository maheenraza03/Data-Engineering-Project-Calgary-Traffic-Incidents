# Data-Engineering-Project-Calgary-Traffic-Incidents

An end-to-end ETL pipeline that extracts Calgary traffic incident data from a public API on the City of Calgary website, transforms and validates the data with Python, loads it into PostgreSQL, and analyzes the data using SQL and Tableau.

## Tech Stack

* **Python**

  * Pandas
  * Requests
  * SQLAlchemy
  * OpenPyXL
* **PostgreSQL**
* **SQL**
* **Tableau Public**
* **Git & GitHub**

## Pipeline

```text
API
 ↓
Extraction
 ↓
Transformation & Data Quality
 ↓
PostgreSQL
 ↓
SQL Analysis & Views
 ↓
Tableau Dashboard Visualization
```

## Project Structure

```text
├── extraction.py
├── transformation.py
├── loading.py
├── calgary_traffic_incidents.xlsx
├── sql/
│   ├── data_quality.sql
│   ├── analysis.sql
│   └── summary_views.sql
└── README.md
```

## Running the Project

Install dependencies:

```bash
pip install pandas openpyxl sqlalchemy psycopg2-binary requests
```

Run the pipeline:

```bash
python extraction.py
python transformation.py
python loading.py
```

SQL scripts can be executed through PostgreSQL or pgAdmin for data quality checks, analysis, and reusable views.

## Dashboard

The processed data is visualized in Tableau Public.

## Future Improvements

* Automate scheduled data extraction
* Implement incremental data loading
* Add automated data-quality tests
* Improve pipeline logging
* Expand dashboard analytics
