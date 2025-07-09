# Installazioine ed importazione librerie
!pip install pandas matplotlib seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Cariacamento dataset
df = pd.read_csv("calorie_alimentari_settimana.csv")

# Visualizzazione dati (prime ed ultime righe)
print("Primi ed ultimi dati del dataset:")
print(df.head(); df.tail())
