SECOND_ETL_PIPELINE - README

This project is a simple Extract–Transform–Load (ETL) pipeline built using Python and PostgreSQL.
The purpose of this pipeline is to read multiple daily CSV files from the data/ folder, combine them,
clean the data, and load it into a PostgreSQL table.

---
PROJECT PURPOSE
- Collect CSV files from data folder
- Merge them
- Clean (drop nulls, convert dates)
- Load into PostgreSQL table landing_daily_sales
- Log operations into Logger_REMARKS.log

---
FOLDER STRUCTURE
SECOND_ETL_PIPELINE/
- data/
- etl.py
- logger_config.py
- requirements.txt
- Dockerfile
- docker-compose.yml
- .dockerignore
- README.md

---
CONCEPTS USED
1. ETL (Extract, Transform, Load)
2. Logging
3. Pandas
4. SQLAlchemy + psycopg2
5. Docker (Postgres container)

---
IN SCOPE
- Read CSV files
- Combine all dataframes
- Clean dataset
- Load to Postgres
- Logging
- Simple Postgres setup via Docker

NOT IN SCOPE
- Advanced validations
- Schema enforcement
- Incremental loads
- Automation/scheduling
- Cloud deployment
- CI/CD pipelines
- Unit tests

---
HOW TO RUN
1. Start Postgres: docker compose up -d postgres
2. Install deps: pip install -r requirements.txt
3. Run ETL: python etl.py
4. Check logs: Logger_REMARKS.log
5. Verify Postgres table: landing_daily_sales

---

Sojan Ojha

