import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat data dari file Excel
file_path = "Data Grafika Komputer.xlsx"  # Pastikan file berada di direktori yang sama
df = pd.read_excel(file_path)

# Pastikan semua data numerik
df[["CPMK012", "CPMK031", "CPMK071", "CPMK072"]] = df[["CPMK012", "CPMK031", "CPMK071", "CPMK072"]].apply(pd.to_numeric, errors='coerce')

# Mengatur data untuk Heatmap
heatmap_data = df.set_index("ID")[["CPMK012", "CPMK031", "CPMK071", "CPMK072"]]

# Membuat Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt=".0f", linewidths=0.5)

# Label dan judul
plt.xlabel("CPMK")
plt.ylabel("ID Mahasiswa")
plt.title("Heatmap Chart CPMK Mahasiswa")
plt.show()
