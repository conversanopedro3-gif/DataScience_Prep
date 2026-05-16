# Chemical Inventory Data Pipeline & BI Automation

Welcome to my technical portfolio. This repository contains practical implementations of data pipelines, data cleaning, and business intelligence reporting using Python for supply chain and laboratory metrics.

## 🚀 Professional Profile
**Aspiring Data Scientist & Automation Developer**
Specialized in building automated data pipelines, data ingestion architectures, and database normalization using Python. Practical experience optimizing data consistency through missing value handling (statistical imputation), redundancy removal, and generating structured corporate reports (*DataFrames*, Excel, CSV) alongside dynamic visualizations with *Matplotlib*.

* **Core Technical Stack:** Python, Pandas, NumPy, Matplotlib, SQLite, Git/GitHub, VS Code.

---

## 📊 Project Breakdown: Laboratory SKU Pipeline (`practica_pandas.py`)
In this project, I developed a script that simulates a corporate data ingestion and cleaning process for manufacturing and chemical product metrics (SKUs):

1. **Data Normalization:** Cleaned typographical errors and structural inconsistencies in product codes using `.replace()`.
2. **Deduplication:** Dropped redundant rows to ensure accurate business reporting via `.drop_duplicates()`.
3. **Statistical Imputation:** Handled missing chemical concentration values (`NaN`) by calculating and injecting the dataset's mathematical mean via `.fillna()`.
4. **Strategic Aggregation:** Implemented `.groupby()` and `.agg()` to generate a high-level executive summary (average price, mean concentration, and stock volume per category).
5. **Automated Reporting:** Programmed the system to automatically export production-ready reports in Excel (`.xlsx`), CSV, and a visual bar chart (`.png`) for stakeholders.
