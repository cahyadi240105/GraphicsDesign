import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load file Excel
file_path = "HeatMap/Data Grafika Komputer.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

#Menghapus kolom "No" dan menjadikan "ID" sebagai indeks
df = df.drop(columns=["No"]).set_index("ID")

#Pastikan ID dalam format string agar tidak diformat ulang
df.index = df.index.astype(str)

#Mengubah nilai CPMK071 untuk ID tertentu
df.loc["2101020103", "CPMK071"] = 7.1
df.loc["2201020086", "CPMK071"] = 7.1

#Membuat heatmap
plt.figure(figsize=(12, 15))
sns.heatmap(df, annot=True, cmap="coolwarm", linewidths=0.5, fmt="g")

#Menambahkan judul
plt.title("\nHeatmap Nilai CPMK per ID", fontsize=14)

#Simpan gambar heatmap
plt.savefig("Heatmap_Nilai_CPMK.png", dpi=600, bbox_inches="tight", pad_inches=0)

#Menampilkan grafik
plt.show()