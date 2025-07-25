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

# Calcola la somma settimanale
somma_settimanale = df.groupby("Settimana")["PesoMedioSollevato_kg"].sum().reset_index()
print("\nSomma settimanale dei pesi sollevati:")
print(somma_settimanale)

# Grafico: Andamento settimanale
plt.figure(figsize=(10, 5))

sns.lineplot(data=media_settimanale, x="Settimana", y="PesoMedioSollevato_kg",
             color="green", marker="o" ,markersize=10)
plt.title("Peso medio sollevato per settimana")
plt.xlabel("Settimana")
plt.ylabel("Peso Medio (kg)")
plt.xticks(media_settimanale["Settimana"], rotation=45)
plt.yticks(range(30, 60, 5))
plt.grid(True)
plt.tight_layout()
plt.show()

# Grafico a barre per ogni giorno
plt.figure(figsize=(12, 6))

custom_palette = sns.color_palette("viridis", n_colors=len(df['Settimana'].unique()))
sns.barplot(data=df, x="Giorno", y="PesoMedioSollevato_kg", hue="Settimana", palette=custom_palette)

plt.title("Confronto peso sollevato tra le settimane")
plt.xlabel("Giorno")
plt.ylabel("Peso Medio (kg)")
plt.legend(title="Settimana")
plt.grid(True)
plt.tight_layout()
plt.show()
