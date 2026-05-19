import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import pandas as pd
import random
import time

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)

print("--- 🚀 AVVIO SCRAPER BLINDATO SU NOTINO ---")

options = uc.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
# Aggiungiamo un'impostazione per far finta di essere un computer con uno schermo reale
options.add_argument('--window-size=1920,1080')
driver = uc.Chrome(options=options)

lista_profumi_totali = []

try:
    for pagina in range(1, 4):
        # URL corretta per la paginazione di Notino
        URL_DINAMICA = f"https://www.notino.it/profumi-uomo/?p={pagina}"
        
        print(f"\nNavigazione invisibile su NOTINO - PAGINA {pagina}: {URL_DINAMICA}")
        driver.get(URL_DINAMICA)
        
        # Aspettiamo che la pagina si carichi e facciamo un piccolo scroll per svegliare il sito
        time.sleep(6)
        driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(2)
        
        html_sito = driver.page_source
        sopa = BeautifulSoup(html_sito, 'html.parser')
        
        # STRATEGIA BLINDATA: Invece di usare le classi strane, cerchiamo tutti i link (tag 'a') 
        # che portano a un profumo (le loro URL contengono sempre il brand o la parola chiave)
        tutti_i_link = sopa.find_all('a')
        
        contatore_pagina = 0
        
        for link in tutti_i_link:
            # Prendiamo il testo dentro il link
            testo_link = link.get_text().strip()
            href_link = link.get('href', '')
            
            # Filtro intelligente: un vero titolo di un profumo ha il testo lungo e il link non deve essere vuoto
            # Evitiamo i link dei menu o del carrello
            if len(testo_link) < 15 or not href_link or "profumi-uomo" in href_link or "javascript" in href_link:
                continue
            
            # Pulizia del testo per evitare doppioni disordinati
            nome_profumo = " ".join(testo_link.split())
            
            # Cerchiamo il prezzo salendo al contenitore della griglia
            contenitore = link.find_parent('div')
            prezzo_reale = "Da verificare"
            
            if contenitore:
                # Cerchiamo qualsiasi testo che contenga il simbolo € vicino al prodotto
                testo_box = contenitore.get_text()
                for parola in testo_box.split():
                    if "€" in parola:
                        prezzo_reale = parola.strip()
                        break
            
            vendite_casuali = random.randint(15, 600)
            
            lista_profumi_totali.append({
                "Profumo": nome_profumo,
                "Prezzo": prezzo_reale,
                "Unita_Vendute_Simulate": vendite_casuali
            })
            contatore_pagina += 1
            
        print(f"Fine NOTINO - PAGINA {pagina}: Estratti {contatore_pagina} potenziali prodotti.")
        time.sleep(3)

    driver.quit()

    if lista_profumi_totali:
        # Raggruppiamo ed eliminiamo i duplicati reali
        df = pd.DataFrame(lista_profumi_totali).drop_duplicates(subset=['Profumo'])
        # Teniamo solo le righe che assomigliano davvero a dei prodotti (scartando scritte di servizio)
        df = df[df['Profumo'].str.len() > 20]
        df_ordinato = df.sort_values(by='Unita_Vendute_Simulate', ascending=False)
        
        print("\n" + "="*100)
        print("📊               MAXI-REPORT NOTINO (PAGINE 1-3) - COMPILATO CON SUCCESSO              ")
        print("="*100)
        print(df_ordinato.head(30).to_string(index=False)) # Mostriamo i primi 30 nel terminale
        print("="*100 + "\n")
        
        df_ordinato.to_csv("C:/DataScience_Prep/Report_Notino_MultiPagina.csv", index=False)
        print(f"🏆 CE L'ABBIAMO FATTA! Salvati {len(df_ordinato)} profumi unici nel file CSV.")
    else:
        print("❌ Il sistema di protezione di Notino ha bloccato la lettura dei tag generali.")

except Exception as e:
    print(f"❌ Errore: {e}")
    try:
        driver.quit()
    except:
        pass
