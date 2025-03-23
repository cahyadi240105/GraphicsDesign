import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat data dari file Excel
file_path = "Data Grafika Komputer.xlsx"  # Pastikan file berada di direktori yang sama
df = pd.read_excel(file_path)

# Membuat Bubble Chart
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    df["CPMK012"], df["CPMK031"],  
    s=df["CPMK071"] * 10,  # Ukuran bubble berdasarkan CPMK071 (dikalikan agar terlihat lebih besar)
    c=df["CPMK072"],  # Warna bubble berdasarkan CPMK072
    cmap="coolwarm", alpha=0.7, edgecolors="k"
)

# Menambahkan color bar
plt.colorbar(label="CPMK072")

# Label dan judul
plt.xlabel("CPMK012")
plt.ylabel("CPMK031")
plt.title("Bubble Chart: CPMK012, CPMK031, CPMK071, dan CPMK072")
plt.grid(True)

# Menampilkan plot
plt.show()
