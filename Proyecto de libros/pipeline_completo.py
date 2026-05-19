import os
import pandas as pd
import matplotlib.pyplot as plt

print("--- INICIANDO PIPELINE DE DATOS UNIFICADO (ETL) ---")

# PASO 1: EJECUTAR EL BOT DE EXTRACCIÓN (EXTRACT)
# Llamamos al script del bot para que vaya a internet y descargue los datos frescos
print("\n[1/3] Lanzando el Bot Scraper para obtener datos en vivo...")
os.system("python scraper_libros.py")

# Definimos la ruta del archivo que genera el bot
RUTA_CSV = "C:/DataScience_Prep/Inventario_Libros_Extraido.csv"

# PASO 2: LOGICA DE NEGOCIO Y PROCESAMIENTO CON PANDAS (TRANSFORM)
if os.path.exists(RUTA_CSV):
    print("\n[2/3] Archivo detectado con éxito. Iniciando transformación analítica...")
    
    # Cargamos los datos extraídos de internet
    df_libros = pd.read_csv(RUTA_CSV)
    
    # Análisis estadístico descriptivo del mercado de libros
    precio_medio = df_libros['Precio_EUR'].mean()
    precio_maximo = df_libros['Precio_EUR'].max()
    precio_minimo = df_libros['Precio_EUR'].min()
    total_libros = len(df_libros)
    
    # Encontramos cuáles son los libros más caros y baratos
    libro_caro = df_libros.loc[df_libros['Precio_EUR'].idxmax(), 'Titulo_Libro']
    libro_barato = df_libros.loc[df_libros['Precio_EUR'].idxmin(), 'Titulo_Libro']
    
    print("\n==================================================")
    print("      RESUMEN EJECUTIVO DE LA TIENDA ONLINE       ")
    print("==================================================")
    print(f"• Volumen de artículos analizados: {total_libros} libros.")
    print(f"• Precio Medio de catálogo: {precio_medio:.2f} EUR")
    print(f"• Producto Líder (Más Caro): {libro_caro} ({precio_maximo:.2f} EUR)")
    print(f"• Producto de Entrada (Más Barato): {libro_barato} ({precio_minimo:.2f} EUR)")
    print("==================================================\n")
    
    # PASO 3: GENERACIÓN DE REPORTES Y VISUALIZACIÓN (LOAD)
    print("[3/3] Generando reportes ejecutivos y gráficos...")
    
    # Creamos una segmentación de precios por rangos (Lógica de negocio)
    # Libros baratos (<40€), estándar (40€-50€) y premium (>50€)
    bins = [0, 40, 50, 100]
    labels = ['Económico (<40€)', 'Estándar (40€-50€)', 'Premium (>50€)']
    df_libros['Rango_Precio'] = pd.cut(df_libros['Precio_EUR'], bins=bins, labels=labels)
    
    conteos = df_libros['Rango_Precio'].value_counts().reindex(labels)
    
    # Graficamos la distribución de catálogo con Matplotlib
    plt.figure(figsize=(8, 5))
    conteos.plot(kind='bar', color=['#2ecc71', '#3498db', '#e74c3c'], edgecolor='black')
    
    plt.title("Distribución de Libros por Rango de Precio (Datos Reales)")
    plt.xlabel("Segmento de Mercado")
    plt.ylabel("Cantidad de Títulos")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.xticks(rotation=0)
    plt.tight_layout()
    
    # Guardamos el gráfico estadístico del mercado real
    plt.savefig("C:/DataScience_Prep/Grafico_Mercado_Libros.png", dpi=300)
    
    print("¡Pipeline finalizado con éxito total!")
    print("-> Gráfico guardado como 'Grafico_Mercado_Libros.png'")
    
else:
    print(f"[ERROR] No se pudo encontrar el archivo {RUTA_CSV}. El bot falló.")
