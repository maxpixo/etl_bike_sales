# 🚴 ETL Pipeline: Bike Sales in Europe

This is a production-ready ETL pipeline built in Python using Pandas and PostgreSQL. It extracts bike sales data from a Kaggle dataset, transforms it using Pandas, and loads it into a PostgreSQL data warehouse using `psycopg2`.

---

## 📦 Project Overview

| Step      | Description                                                       |
| --------- | ----------------------------------------------------------------- |
| Extract   | Reads a raw `.csv` file (`Sales.csv`) from the `data/raw/` folder |
| Transform | Cleans, formats, and standardizes the data using `pandas`         |
| Load      | Loads the clean data into a PostgreSQL table using `psycopg2`     |

The project includes modular code, environment variables, unit tests, and is ready for deployment or GitHub portfolio use.

---

## 🏗 Project Structure

```
etl_bike_sales/
│
├── data/
│   └── raw/                      # Raw Kaggle CSV goes here (Sales.csv)
│
├── etl_bike_sales/               # Source code package
│   ├── config/                   # DB config using dotenv
│   │   └── settings.py
│   ├── extract/                  # Extract module
│   │   └── csv_extractor.py
│   ├── transform/                # Transform module
│   │   └── transformer.py
│   ├── load/                     # Load module using psycopg2
│   │   └── postgres_loader.py
│   └── pipeline.py               # ETL pipeline controller
│
├── tests/                        # Unit tests for each stage
│   ├── test_extract.py
│   ├── test_transform.py
│   ├── test_load.py
│
├── run_etl.py                    # Entry point to run the full pipeline
├── .env                          # Environment variables (not committed)
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignored files/folders
└── README.md                     # Project documentation
```

---

## 📊 Dataset

- **Name:** [Bike Sales in Europe](https://www.kaggle.com/datasets/anujgupta/bike-sales-in-europe)
- **File:** `Sales.csv`
- **Rows:** 113,036
- **Columns:** 18 fields including `Date`, `Customer_Age`, `Product`, `Revenue`, etc.

---

## ⚙️ Setup Instructions

### 1. 🔧 Clone the repo

```bash
git clone https://github.com/your-username/etl_bike_sales.git
cd etl_bike_sales
```

### 2. 🐍 Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. 📦 Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. 🛠 Configure environment variables

Create a `.env` file in the project root:

```ini
PG_HOST=localhost
PG_PORT=5432
PG_USER=postgres
PG_PASSWORD=yourpassword
PG_DB=etl_bikes
```

### 5. 🧪 Verify PostgreSQL is running

Make sure PostgreSQL is installed and running on your machine. Create the database if needed:

```bash
createdb etl_bikes
```

---

## 🚀 Running the ETL Pipeline

1. Place `Sales.csv` inside `data/raw/`
2. Run the pipeline:

```bash
python run_etl.py
```

### Expected Output:

```
######## Starting ETL Pipeline...
############# Extracted 113036 rows from data/raw/Sales.csv #############
Transformed DataFrame with 113036 rows and 18 columns
✅ Inserted 113036 rows into table 'bikes'
ETL Pipeline completed successfully
```

---

## 🧪 Running Tests

To validate components individually:

```bash
python -m unittest discover tests
```

Or run a specific test:

```bash
python -m unittest tests/test_load.py
```

---

## 🛠 Technologies Used

- Python 3.11+
- pandas
- psycopg2-binary
- dotenv
- PostgreSQL
- unittest

---

## ✅ Future Enhancements

- Use `COPY FROM` for bulk loading performance
- Add CI/CD workflow using GitHub Actions
- Create Power BI or Tableau dashboard from PostgreSQL table
- Add logging and retry logic for robustness
- Export cleaned data to a data lake (e.g., Parquet in S3 or ADLS)

---

## 🙌 Credits

- Dataset: [Anuj Gupta on Kaggle](https://www.kaggle.com/datasets/anujgupta/bike-sales-in-europe)
- Developed by: **Mahmoud Abouzeid**

---

## 🔒 Disclaimer

Do not commit your `.env` file or credentials to GitHub. Use `.gitignore` to exclude sensitive information.

---

## 📂 License

MIT License – free to use, modify, and share.
