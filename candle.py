import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Memuat data dari file Excel
file_path = "Data Grafika Komputer.xlsx"  # Pastikan file berada di direktori yang sama
df = pd.read_excel(file_path)

# Mengatur data untuk Candlestick Chart
df_candle = df[["CPMK012", "CPMK031", "CPMK071", "CPMK072"]]
df_candle.columns = ["Open", "High", "Low", "Close"]

# Menambahkan index berupa tanggal (Dummy Date untuk keperluan plotting)
df_candle.index = pd.date_range(start="2024-01-01", periods=len(df), freq="D")

# Membuat Candlestick Chart
mpf.plot(df_candle, type='candle', style='charles', title='Candlestick Chart CPMK', ylabel='Nilai CPMK')