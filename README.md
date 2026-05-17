# Chemical Inventory Data Pipeline & BI Automation

Welcome to my technical portfolio. This repository contains practical implementations of web scraping, automated data pipelines, data cleaning, and business intelligence reporting using Python for supply chain, e-commerce, and laboratory metrics.

## 🚀 Professional Profile
**Aspiring Data Scientist & Automation Developer**
Specialized in building automated data pipelines, data ingestion architectures, web scraping bots, and database normalization using Python. Practical experience optimizing data consistency through missing value handling (statistical imputation), redundancy removal, and generating structured corporate reports (*DataFrames*, Excel, CSV) alongside dynamic visualizations with *Matplotlib*.

* **Core Technical Stack:** Python, Pandas, NumPy, BeautifulSoup4, Requests, Matplotlib, SQLite, Git/GitHub, VS Code.

---

## 📊 Project 1: Laboratory SKU Pipeline (`practica_pandas.py`)
In this project, I developed a script that simulates a corporate data ingestion and cleaning process for manufacturing and chemical product metrics (SKUs):

1. **Data Normalization:** Cleaned typographical errors and structural inconsistencies in product codes using `.replace()`.
2. **Deduplication:** Dropped redundant rows to ensure accurate business reporting via `.drop_duplicates()`.
3. **Statistical Imputation:** Handled missing chemical concentration values (`NaN`) by calculating and injecting the dataset's mathematical mean via `.fillna()`.
4. **Strategic Aggregation:** Implemented `.groupby()` and `.agg()` to generate a high-level executive summary (average price, mean concentration, and stock volume per category).
5. **Automated Reporting:** Programmed the system to automatically export production-ready reports in Excel (`.xlsx`), CSV, and a visual bar chart (`.png`) for stakeholders.

---

## 🕷️ Project 2: Automated E-Commerce Web Scraper (`scraper_libros.py`)
In this project, I engineered an autonomous web scraping pipeline designed to harvest live inventory and pricing metrics from a simulated commercial marketplace:

1. **HTTP Ingestion:** Programmed network requests using `requests` with customized *User-Agent* headers to mimic human browser behavior and bypass server-side connection blocks.
2. **HTML Parsing & Extraction:** Utilized `BeautifulSoup4` to traverse the DOM tree, targeting specific HTML tags (`<article>`, `<h3>`, `<p>`) to extract raw titles and pricing elements.
3. **Encoding & Text Sanitization:** Implemented in-line string cleaning logic (`.replace()`, `.strip()`) to eliminate corrupt encoding artifacts (such as ghost characters like `Â`) and currency symbols, safely converting text streams into clean numeric data types (`float`).
4. **Structured Storage:** Formatted the unstructured web data into a tabular *Pandas DataFrame* and automated its compilation into a clean, production-ready `Inventario_Libros_Extraido.csv` report.
