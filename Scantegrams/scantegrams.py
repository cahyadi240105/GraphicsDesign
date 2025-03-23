import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Memuat data dari file Excel
file_path = "Data Grafika Komputer.xlsx" 
df = pd.read_excel(file_path)

# Menentukan kategori CPMK
categories = ["CPMK012", "CPMK031", "CPMK071", "CPMK072"]

# Membuat figure
fig, ax = plt.subplots(figsize=(10, 6))

# Warna untuk setiap kategori CPMK
colors = ["red", "blue", "green", "purple"]

# Loop untuk setiap kategori CPMK dan plot data dalam Scattergram
for idx, category in enumerate(categories):
    x = df["ID"].astype(str)  # Menggunakan ID sebagai label sumbu X
    y = df[category]
    ax.scatter(x, y, color=colors[idx], alpha=0.7)

# Menambahkan label dan judul
ax.set_xlabel("ID Mahasiswa")
ax.set_ylabel("Rentang Nilai")
ax.set_title("Pencapaian Nilai CPMK")
plt.xticks(rotation=90, fontsize=6)  # Memiringkan ID untuk keterbacaan

# Menampilkan legenda sejajar dengan nilai CPMK
ax.legend(categories, loc="upper left", bbox_to_anchor=(1, 0.5), title="Kategori CPMK")

# Menampilkan plot
plt.show()
