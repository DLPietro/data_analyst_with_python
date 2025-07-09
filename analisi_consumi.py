# Installazione ed importazione librerie
!pip install pandas matplotlib seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cariacamento dataset
df = pd.read_csv("calorie_alimentari_settimana.csv")

# Visualizzazione dati (prime ed ultime righe)
print("Primi ed ultimi dati del dataset:")
print(df.head(), df.tail())

# Calcolo totale giornaliero di calorie
df['Totale']=df[['Colazione (kcal)', 'Pranzo (kcal)', 'Cena (kcal)', 'Snack (kcal)']].sum(axis=1)

# Calcolo Media
media_calorie = df['Totale'].mean()
print(f"\nMedia di calorie giornaliere: {calorie_medie:.0f} kcal")
