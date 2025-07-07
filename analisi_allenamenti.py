!pip install pandas matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Carica il dataset
df = pd.read_csv("allenamenti_settimana.csv")

# Mostra le prime righe
print("Primi dati del dataset:")
print(df.head())

# Filtra solo i giorni di allenamento effettivo
df_allenamenti = df[df["PesoMedioSollevato_kg"] > 0]

# Calcola il peso medio sollevato
peso_medio = df_allenamenti["PesoMedioSollevato_kg"].mean()
print(f"\nPeso medio sollevato a settimana: {peso_medio:.1f} kg")

# Grafico: Peso sollevato per giorno
plt.figure(figsize=(10,5))
plt.bar(df_allenamenti["Giorno"], df_allenamenti["PesoMedioSollevato_kg"], color='skyblue')
plt.title("Peso Medio Sollevato per Giorno")
plt.xlabel("Giorno")
plt.ylabel("Peso Medio (kg)")
plt.grid(True)
plt.show()
