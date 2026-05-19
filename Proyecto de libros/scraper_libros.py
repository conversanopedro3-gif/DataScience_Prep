import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Configuración de la URL de la tienda simulada
URL_TIENDA = "http://books.toscrape.com/"

# Añadimos 'Headers' para que Python se identifique de forma educada ante el servidor
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("--- INICIANDO EXTRACCIÓN DE DATOS DE INTERNET ---")

# 2. El bot hace la petición a la web
respuesta = requests.get(URL_TIENDA, headers=headers)

# Verificamos si la web nos dio permiso para entrar (Status Code 200 significa éxito)
if respuesta.status_code == 200:
    print("¡Conexión exitosa al servidor!")
    
    # 3. BeautifulSoup procesa el código HTML en bruto de la página web
    sopa = BeautifulSoup(respuesta.text, 'html.parser')
    
    # Listas vacías donde el bot irá guardando lo que encuentre
    lista_titulos = []
    lista_precios = []
    
    # 4. Localizamos las "tarjetas" contenedoras de cada libro en el HTML
    libros = sopa.find_all('article', class_='product_pod')
    
    print(f"Detectados {len(libros)} libros en la página principal. Extrayendo información...")
    
    for libro in libros:
        # Extraemos el título del libro (buscando la etiqueta <h3> y luego el enlace <a>)
        titulo = libro.h3.a['title']
        
        # Extraemos el precio en texto (buscando el párrafo con la clase 'price_color')
        precio_texto = libro.find('p', class_='price_color').text
        
        # LIMPIEZA DE DATOS CRÍTICA: Quitamos el símbolo de la libra (£) y el carácter 'Â' rebelde
        precio_limpio = precio_texto.replace('£', '').replace('Â', '').strip()
        
        # Guardamos los datos limpios en nuestras listas
        lista_titulos.append(titulo)
        lista_precios.append(float(precio_limpio)) # Lo convertimos a número decimal (float)
        
    # 5. ESTRUCTURACIÓN: Pasamos las listas al formato estrella, un DataFrame de Pandas
    datos_tienda = {
        'Titulo_Libro': lista_titulos,
        'Precio_EUR': lista_precios
    }
    df_libros = pd.DataFrame(datos_tienda)
    
    print("\n--- VISTA PREVIA DE LOS DATOS EXTRAÍDOS POR EL BOT ---")
    print(df_libros.head()) # Muestra las primeras 5 filas en consola
    
    # 6. AUTOMATIZACIÓN: Guardamos los datos de internet directamente en un archivo CSV limpio
    df_libros.to_csv('C:/DataScience_Prep/Inventario_Libros_Extraido.csv', index=False)
    print("\n¡Éxito total! Archivo 'Inventario_Libros_Extraido.csv' guardado en tu PC.")

else:
    print(f"Error de conexión. Código de estado del servidor: {respuesta.status_code}")
