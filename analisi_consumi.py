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

# Calcolo del totale settimanale per ciscun tipo di pasto
colazioni_totali = df['Colazione (kcal)'].sum()
pranzi_totali = df['Pranzo (kcal)'].sum()
cene_totali = df['Cena (kcal)'].sum()
spuntini_totali = df['Spuntino (kcal)'].sum()

# Preaparazione dati per il grafico a torta
labels = ['Colazione', 'Pranzo', 'Cena', 'Spuntino']
sizes = [colazioni_totali, pranzi_totali, cene_totali, spuntini_totali]
colors = sns.color_palette('pastel')

# Creazione Grafico a Torta
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title("Distribuzione delle calorie settimanali")
plt.axis('equal')  # Grafico Circolare
plt.show()
