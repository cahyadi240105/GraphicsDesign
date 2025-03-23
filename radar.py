import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Memuat data dari file Excel
file_path = "Data Grafika Komputer.xlsx"  # Pastikan file berada di direktori yang sama
df = pd.read_excel(file_path)

# Menentukan kategori CPMK
categories = ["CPMK012", "CPMK031", "CPMK071", "CPMK072"]
num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Menutup lingkaran

# Membuat figure
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Warna untuk setiap CPMK
colors = ["red", "blue", "green", "purple"]

# Loop untuk setiap mahasiswa (latar belakang abu-abu)
for i, row in df.iterrows():
    values = row[categories].values.tolist()
    values += values[:1]  # Menutup lingkaran
    ax.plot(angles, values, linewidth=0.8, linestyle='dotted', alpha=0.5, color="gray", label=row["ID"] if i < 10 else "")

# Loop untuk setiap kategori CPMK, menampilkan rata-rata dengan warna berbeda
for idx, category in enumerate(categories):
    avg_value = df[category].mean()
    avg_values = [avg_value] * num_vars  # Samakan jumlah titik
    avg_values += avg_values[:1]  # Menutup lingkaran
    ax.plot(angles, avg_values, label=category, linewidth=2, linestyle='solid', color=colors[idx])

# Menambahkan label kategori
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# Menampilkan legenda untuk setiap CPMK
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize="small", title="Kategori CPMK")

# Judul
plt.title("Spider Chart dengan Warna Berdasarkan CPMK dan ID Mahasiswa")
plt.show()
