!pip install pandas matplotlib seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carica il dataset
df = pd.read_csv("progressi_allenamenti.csv")

# Mostra prime righe
print("Primi dati del dataset:")
print(df.head())

# Calcola la media settimanale
media_settimanale = df.groupby("Settimana")["PesoMedioSollevato_kg"].mean().reset_index()
print("\nMedia settimanale dei pesi sollevati:")
print(media_settimanale)

# Grafico: Andamento settimanale
plt.figure(figsize=(10, 5))
sns.lineplot(data=media_settimanale, x="Settimana", y="PesoMedioSollevato_kg", marker='o')
plt.title("Andamento medio del peso sollevato per settimana")
plt.xlabel("Settimana")
plt.ylabel("Peso Medio (kg)")
plt.grid(True)
plt.show()

# Grafico a barre per ogni giorno
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="Giorno", y="PesoMedioSollevato_kg", hue="Settimana")
plt.title("Confronto peso sollevato tra le settimane")
plt.xlabel("Giorno")
plt.ylabel("Peso Medio (kg)")
plt.legend(title="Settimana")
plt.grid(True)
plt.tight_layout()
plt.show()
