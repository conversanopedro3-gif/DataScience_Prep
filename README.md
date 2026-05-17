# Corporate Data Pipelines, Web Scraping & BI Automation

Welcome to my technical portfolio. This repository showcases production-ready implementations of autonomous web scraping, complete ETL pipelines, statistical data sanitization, and automated Business Intelligence (BI) reporting using Python.

## 🚀 Professional Profile
**Aspiring Data Scientist & Automation Developer**
Specialized in engineering end-to-end data architectures, automated ingestion pipelines, and structural web scrapers using Python. Experienced in optimizing dataset integrity through redundancy removal, missing value handling via statistical imputation, and generating multi-format executive summaries (DataFrames, Excel, CSV) coupled with insightful business visualizations using *Matplotlib*.

* **Core Technical Stack:** Python, Pandas, NumPy, BeautifulSoup4, Requests, Matplotlib, Git/GitHub, VS Code.

---

## 🏗️ Project Portfolio Breakdown

### 📊 1. Laboratory SKU Data Ingestion Pipeline (`practica_pandas.py`)
A simulated corporate data cleaning script engineered to normalize structural and typographical anomalies in manufacturing records:
* **Data Normalization & Deduplication:** Cleansed categorical inconsistencies via `.replace()` and pruned redundant rows using `.drop_duplicates()`.
* **Statistical Imputation:** Mitigated missing chemical concentration metrics (`NaN`) by calculating and injecting the mathematical mean of the feature vector via `.fillna()`.
* **Executive Aggregation:** Applied `.groupby()` and `.agg()` matrices to output high-level insights (average pricing, concentration bounds, and inventory volume per SKU class).

### 🕷️ 2. Autonomous Market Intelligence Scraper (`scraper_libros.py`)
An independent web crawling bot built to dynamically harvest commercial intelligence and pricing catalog data from live web servers:
* **HTTP Ingestion:** Engineered robust network requests utilizing custom *User-Agent* mapping to simulate human behavior and prevent connection blocks.
* **DOM Traversal:** Used `BeautifulSoup4` to target structural HTML coordinates (`<article>`, `<h3>`, `<p>`) for mass data extraction.
* **Text Sanitization & Type Casting:** Cleaned formatting artifacts and corrupt string tokens (e.g., `Â`, `£`) using text-replacement vectors, safely casting the raw streams into operational `float` datatypes.

### ⚙️ 3. Unified End-to-End ETL Data Pipeline (`pipeline_completo.py`)
An advanced orquestrator script that unifies the collection and analysis scripts into a production-ready **Extract, Transform, Load (ETL)** system:
* **Orchestration:** Automates the execution of the web scraper to fetch live market entries from the network layer.
* **BI Transformation:** Ingests the output dataset, executes predictive segmentations (Económico, Estándar, Premium) using custom binning constraints (`pd.cut()`), and runs a descriptive analytical query across prices.
* **Automated Visual Reporting:** Generates an executive summary directly to the terminal alongside an automated distribution chart (`Grafico_Mercado_Libros.png`) built with *Matplotlib*.
