import pandas as pd

print("--- 📊 AVVIO ANALISI DATI CON PANDAS ---")

# 1. Carichiamo il dataset perfetto
PERCORSO_FILE = "C:/DataScience_Prep/Report_Notino_PERFETTO.csv"
df = pd.read_csv(PERCORSO_FILE)

# CORREZIONE: Ora leggiamo la colonna corretta 'Prezzo_EUR' che crea lo spazzino
df['Prezzo_Numerico'] = df['Prezzo_EUR'].str.replace(' €', '').str.replace(',', '.').astype(float)

# 2. CALCOLI STATISTICI
prezzo_medio = df['Prezzo_Numerico'].mean()
totale_vendite = df['Unita_Vendute'].sum() # Aggiornato anche il nome di questa colonna

# Troviamo le righe del record massimo e minimo
profumo_caro = df.loc[df['Prezzo_Numerico'].idxmax()]
profumo_economico = df.loc[df['Prezzo_Numerico'].idxmin()]

# Raggruppamento per marca (Somma delle vendite)
classifica_marche = df.groupby('Marca')['Unita_Vendute'].sum().sort_values(ascending=False)

# 3. STAMPA DEL REPORT SUL TERMINALE
print("\n" + "="*60)
print("📈               KPI & STATISTICHE DI MERCATO               ")
print("="*60)
print(f"💵 Prezzo Medio dei Profumi: {prezzo_medio:.2f} €")
print(f"📦 Unità Totali Movimentate: {totale_vendite} pezzi")
print(f"💎 Fragranza Top di Gamma:   {profumo_caro['Marca']} - {profumo_caro['Profumo']} ({profumo_caro['Prezzo_EUR']})")
print(f"🏷️ Fragranza Entry Level:    {profumo_economico['Marca']} - {profumo_economico['Profumo']} ({profumo_economico['Prezzo_EUR']})")
print("="*60)

print("\n👑 CLASSIFICA MARCHE PER UNITÀ VENDUTE:")
print(classifica_marche.to_string())
print("="*60 + "\n")
