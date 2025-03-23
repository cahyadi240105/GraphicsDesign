import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Memuat data dari file Excel
file_path = "Data Grafika Komputer.xlsx"  # Pastikan file berada di direktori yang sama
df = pd.read_excel(file_path)

# Menentukan kategori CPMK
categories = ["CPMK012", "CPMK031", "CPMK071", "CPMK072"]

# Membuat figure
fig, ax = plt.subplots(figsize=(10, 6))

# Warna untuk setiap kategori CPMK
colors = ["red", "blue", "green", "purple"]

# Loop untuk setiap kategori CPMK
for idx, category in enumerate(categories):
    x = df["ID"].astype(str)  # Menggunakan ID sebagai label sumbu X
    y = df[category]
    ax.vlines(x, 0, y, color=colors[idx], alpha=0.5, linewidth=2)
    ax.scatter(x, y, color=colors[idx], alpha=1, label=category)

# Menambahkan label dan judul
ax.set_xlabel("ID Mahasiswa")
ax.set_ylabel("Nilai CPMK")
ax.set_title("Lollipop Chart CPMK Mahasiswa")
plt.xticks(rotation=90, fontsize=8)  # Memiringkan ID untuk keterbacaan
ax.legend(title="Kategori CPMK")

# Menampilkan plot
plt.show()
