import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\zigao\OneDrive - Univerza v Ljubljani\Documents\krevs_23_suša.csv")


plt.figure(figsize=(15, 12))
plt.plot(df['Leto2'], df['km22'], marker='o', linestyle='-', color='b', label='podatki časovne vrste')
plt.title('Obseg suše po letih', weight = "bold")
plt.xlabel('Leto')
plt.ylabel('Površina (km2)')
plt.legend()
plt.grid(True)
plt.show()
