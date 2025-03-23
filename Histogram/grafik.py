import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = "Histogram/dataTBP.csv"
df = pd.read_csv(file_path)

df.columns = df.columns.str.replace("\t", "")

df['ID'] = df['ID'].astype(str)

x = np.arange(len(df['ID'])) 
width = 0.15  

colors = ["#FF5733", "#33FF57", "#3357FF", "#F39C12", "#9B59B6", "#E74C3C", "#1ABC9C"]

fig, ax = plt.subplots(figsize=(12, 6))
for i, (cpmk, color) in enumerate(zip(df.columns[1:], colors)):
    bars = ax.bar(x + i * width, df[cpmk], width, label=cpmk, color=color)
    
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, str(int(bar.get_height())), 
                ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_xlabel("ID Mahasiswa")
ax.set_ylabel("Nilai CPMK")
ax.set_title("Histogram CPMK untuk Setiap ID")
ax.set_xticks(x + width * (len(df.columns) - 2) / 2)
ax.set_xticklabels(df['ID'], rotation=90)
ax.legend()
ax.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()
