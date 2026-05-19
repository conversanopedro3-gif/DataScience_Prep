# 🧪 Notino Fragrance Market Scraper & Data Analytics

Este proyecto es una suite completa de **Data Science** y **Web Scraping** diseñada para automatizar la recopilación, limpieza y análisis estadístico del mercado de fragancias masculinas en el e-commerce de Notino.

El proyecto está desarrollado completamente en **Python** y estructurado bajo los estándares profesionales de pipelines de datos.

---

## 🛠️ Estructura del Proyecto

El repositorio está dividido en 3 motores lógicos independientes y un dataset final optimizado:

1. **`scraper_profumi.py` (Extracción de Datos):** Automatiza la navegación web utilizando `undetected-chromedriver` para evadir sistemas anti-bot de forma invisible. Utiliza un ciclo iterativo (`for`) para paginar el catálogo de forma dinámica y captura el código fuente con `BeautifulSoup`.
2. **`pulisci_report.py` (Data Cleaning):** Procesa el texto plano extraído del DOM de la página. Utiliza expresiones regulares (`re`) y `Pandas` para eliminar ruido de fondo, separar las marcas comerciales de los nombres de los productos e aislar los precios reales en formato numérico.
3. **`analizza_dati.py` (Business Intelligence):** Carga la base de datos optimizada y ejecuta cálculos estadísticos en milisegundos utilizando `Pandas` para extraer KPIs de negocio.
4. **`Report_Notino_PERFETTO.csv` (Dataset Optimizado):** El resultado final. Una base de datos estructurada y limpia con información de marcas, nombres de fragancias, precios reales y unidades de venta simuladas.

---

## 📈 KPIs extraídos del Mercado

Tras ejecutar el pipeline completo sobre el catálogo analizado, el procesador estadístico arroja los siguientes indicadores clave de rendimiento:

* 💵 **Precio Medio del Mercado:** ~43.08 €
* 💎 **Fragranza Top de Gama (Más cara):** Yves Saint Laurent - Y Le Parfum (97.30 €)
* 🏷️ **Fragranza Entry Level (Más barata):** Calvin Klein - CK Be (17.70 €)

### 👑 Top Marcas con Mayor Volumen de Ventas (Simuladas)
El análisis con Pandas determinó que el volumen del mercado está liderado por las siguientes marcas:
1. **Calvin Klein** (Mayor volumen de unidades)
2. **Yves Saint Laurent**
3. **Lattafa** (Fragancias árabes en tendencia de crecimiento)

---

## ⚙️ Requisitos e Instalación

Para ejecutar este pipeline localmente, clona este repositorio e instala las dependencias de compatibilidad para entornos avanzados (Python 3.14+):

```bash
python -m pip install undetected-chromedriver beautifulsoup4 pandas setuptools