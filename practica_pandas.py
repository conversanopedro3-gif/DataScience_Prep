import pandas as pd
import matplotlib.pyplot as plt

# 1. Lista de productos limpia con códigos industriales (SKU)
datos_laboratorio = {
    'Producto': ['SKU-Myrcene_v1', 'SKU-Pinene_v1', 'SKU-Limone_v1', 'SKU-Myrcene_v1', 'SKU-Linalool_v2', 'SKU-BetaC_v2'],
    'Concentracion_%': [85, 78, None, 85, 92, 64],
    'Precio_EUR': [45, 40, 50, 45, 60, 35],
    'Categoria': ['Premium', 'Standard', 'Premium', 'Premium', 'Ultra', 'Standard']
}

# 2. Convertimos a DataFrame y corregimos el error (Limone -> Limonene)
df = pd.DataFrame(datos_laboratorio)
df['Producto'] = df['Producto'].replace('SKU-Limone_v1', 'SKU-Limonene_v1')

# 3. Eliminamos duplicados y rellenamos el vacío con la media matemática
df_limpio = df.drop_duplicates()
media_concentracion = df_limpio['Concentracion_%'].mean()
df_final = df_limpio.copy()
df_final['Concentracion_%'] = df_final['Concentracion_%'].fillna(media_concentracion)

# 4. Agrupación estadística de negocio
analisis_categoria = df_final.groupby('Categoria').agg({
    'Precio_EUR': 'mean',
    'Concentracion_%': 'mean',
    'Producto': 'count'
}).rename(columns={'Producto': 'Cantidad_Productos'})

# 5. Exportar reportes técnicos automáticos
df_final.to_excel('C:/DataScience_Prep/Reporte_Productos_Limpio.xlsx', index=False)
productos_top = df_final[(df_final['Categoria'] == 'Premium') & (df_final['Precio_EUR'] > 40)]
productos_top.to_csv('C:/DataScience_Prep/Analisis_Premium_Top.csv', index=False)

# 6. VISUALIZACIÓN: Generar el nuevo gráfico profesional limpio
analisis_categoria['Precio_EUR'].plot(kind='bar', color=['#4CAF50', '#FF9800', '#2196F3'])
plt.title('Precio Medio por Categoria de Producto')
plt.xlabel('Categoria')
plt.ylabel('Precio en EUR')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Guardar la imagen nueva
plt.savefig('C:/DataScience_Prep/Grafico_Precios.png', bbox_inches='tight')
print("¡Pipeline ejecutado con éxito con datos corporativos!")