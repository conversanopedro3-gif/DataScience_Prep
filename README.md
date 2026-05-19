# 📊 Data Science & Web Automation Portfolio

Welcome to my personal Data Science portfolio. This repository contains end-to-end automated pipelines, featuring advanced web scraping, data cleaning, and professional executive reporting.

> 🌍 **Choose your language / Scegli la tua lingua:**
> * [English Version](#-english-version)
> * [Versione Italiana](#-versione-italiana)

---

## 🇬🇧 English Version

### 📂 Repository Structure
The project is fully organized into dedicated directories to maintain a clean environment:
* 📚 **[Proyecto_Libros](./Proyecto_Libros/)**: Book market analysis, visualization, and pandas prototyping.
* 🧴 **[Proyecto_Perfumes](./Proyecto_Perfumes/)**: Notino fragrance market intelligence and automated Excel engine.

---

### 🧴 Project 1: Notino Fragrance Market Analytics

An automated pipeline designed to extract, normalize, and process catalog data from Notino. This engine handles raw layout anomalies and programmatically generates tailored corporate spreadsheet reports.

#### 🚀 Core Features
* **Automated Web Scraping:** Extracts multi-page catalog data dynamically, bypassing layout fragmentation.
* **Deep Data Cleaning:** Normalizes merged text structures (successfully isolating premium brands like *DIOR*, *TOM FORD*, and *Rabanne*), filters layout noise, and parses prices.
* **Programmatic Excel Styling:** Automatically generates styled spreadsheets (`.xlsx`) using `openpyxl`, featuring wide columns (65-character width for names), dark navy headers, zebra striping, and proper accounting currency alignments.

#### 🛠️ Tech Stack & Scripts
* `scraper_profumi.py`: Automated web scraping bot for raw data extraction.
* `pulisci_report.py`: Advanced data cleaning engine and programmatic Excel formatter.
* `analizza_dati.py`: Statistical script computing KPIs and market rankings using Pandas.
* `Report_Notino_PERFETTO.xlsx`: Final polished spreadsheet output.

#### 📈 Key Market KPIs & Insights
* **Total Simulated Volume:** 9,702 pieces managed.
* **Average Fragrance Price:** €47.81
* **Top Premium Model:** Nasomatto - Black Afgano Extrait de Parfum 30ml (€110.60)
* **Market Leader by Volume:** Lattafa (1,414 units)

---

### 📚 Project 2: Book Market Scraper & Analytics

A modular data engineering practice focused on catalog scraping, price distribution, and exploratory data analysis (EDA).

#### 🚀 Core Features
* **Catalog Mining:** Extraction of book titles, pricing structures, and stock availability.
* **Exploratory Analytics:** Data aggregation using Pandas to isolate pricing distribution patterns.
* **Data Visualization:** Generates automated static plots tracking market trends.

#### 🛠️ Tech Stack & Scripts
* `scraper_libros.py`: Book extraction module.
* `practica_pandas.py` & `pipeline_completo.py`: Data analysis and aggregation scripts.
* `Grafico_Precios.png` & `Grafico_Mercado_Libros.png`: Distribution charts.

---

## 🇮🇹 Versione Italiana

### 📂 Struttura del Repository
Il progetto è interamente organizzato in directory dedicate per mantenere l'ambiente pulito:
* 📚 **[Proyecto_Libros](./Proyecto_Libros/)**: Analisi del mercato dei libri, visualizzazione dati e prototipazione Pandas.
* 🧴 **[Proyecto_Perfumes](./Proyecto_Perfumes/)**: Market intelligence delle fragranze Notino e motore Excel automatizzato.

---

### 🧴 Progetto 1: Notino Fragrance Market Analytics

Una pipeline automatizzata progettata per estrarre, normalizzare ed elaborare i dati del catalogo Notino. Questo motore corregge le anomalie del testo grezzo e genera programmaticamente report Excel in stile aziendale.

#### 🚀 Funzionalità Principali
* **Web Scraping Automatizzato:** Estrae dinamicamente i dati del catalogo multi-pagina superando i blocchi di testo uniti del sito.
* **Pulizia Profonda dei Dati:** Normalizza stringhe di testo complesse (separando correttamente marchi premium come *DIOR*, *TOM FORD* e *Rabanne*), rimuove i banner pubblicitari e converte i prezzi.
* **Stile Excel Programmatico:** Genera automaticamente fogli di calcolo (`.xlsx`) stilizzati tramite `openpyxl`, con colonne extra-larghe (65 caratteri per il nome del profumo), intestazioni blu notte, righe alternate (*zebra striping*) e allineamento contabile della valuta.

#### 🛠️ Tecnologie e Script
* `scraper_profumi.py`: Bot per lo scraping automatizzato e l'estrazione dei dati.
* `pulisci_report.py`: Motore avanzato di pulizia dati, spaziatura del testo e formattazione dello stile Excel.
* `analizza_dati.py`: Script di calcolo statistico che elabora i KPI e le classifiche di mercato con Pandas.
* `Report_Notino_PERFETTO.xlsx`: Il file Excel finale formattato automaticamente dal codice.

#### 📈 KPI e Statistiche di Mercato Rilevate
* **Unità Totali Movimentate:** 9.702 pezzi gestiti.
* **Prezzo Medio dei Profumi:** 47,81 €
* **Fragranza Top di Gamma:** Nasomatto - Black Afgano estratto profumato 30 ml (110,60 €)
* **Marchio Leader per Volume:** Lattafa (1.414 unità simulate)

---

### 📚 Progetto 2: Book Market Scraper & Analytics

Una pratica modulare di ingegneria dei dati focalizzata sullo scraping dei cataloghi, sulla distribuzione dei prezzi e sull'analisi esplorativa dei dati (EDA).

#### 🚀 Funzionalità Principali
* **Catalog Mining:** Estrazione di titoli di libri, strutture di prezzo e disponibilità a magazzino.
* **Analisi Esplorativa:** Aggregazione dei dati tramite Pandas per isolare i modelli di distribuzione dei prezzi.
* **Visualizzazione Dati:** Genera grafici statici automatizzati per tracciare i trend di mercato.

#### 🛠️ Tecnologie e Script
* `scraper_libros.py`: Modulo di estrazione dei libri.
* `practica_pandas.py` & `pipeline_completo.py`: Script di analisi e aggregazione dati.
* `Grafico_Precios.png` & `Grafico_Mercado_Libros.png`: Grafici di distribuzione dei prezzi.
