!pip install pandas matplotlib
import pandas as pd

# Carica il dataset
df = pd.read_csv("calorie_settimana.csv")

# Mostra le prime righe
print("Primi dati del dataset:")
print(df.head())

# Calcola la media giornaliera
media_calorie = df["Totale"].mean()
print(f"\nMedia giornaliera di calorie: {media_calorie:.0f} kcal")

# Grafico semplice
df.set_index("Giorno")[["Colazione (kcal)", "Pranzo (kcal)", "Cena (kcal)"]].plot(kind="bar", title="Consumo calorico giornaliero")
