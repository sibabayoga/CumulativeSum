import streamlit as st
import time
import random
import numpy as np
import pandas as pd
import sys

# Set batas rekursi lebih tinggi untuk menghindari RecursionError
sys.setrecursionlimit(10000)

# Fungsi untuk menghitung cumulative sum menggunakan iterasi
def cumulative_sum_iterative(numbers):
    """Menghitung jumlah kumulatif dari array angka menggunakan iterasi."""
    cumulative = []
    current_sum = 0
    for number in numbers:
        current_sum += number
        cumulative.append(current_sum)
    return cumulative

# Fungsi untuk menghitung cumulative sum menggunakan rekursi
def cumulative_sum_recursive(numbers, index=0, current_sum=0, result=None):
    """Menghitung jumlah kumulatif dari array angka menggunakan rekursi."""
    if result is None:
        result = []

    if index == len(numbers):  # Base case
        return result

    current_sum += numbers[index]
    result.append(current_sum)

    return cumulative_sum_recursive(numbers, index + 1, current_sum, result)

# Fungsi untuk menghasilkan daftar angka acak
def generate_random_numbers(count, min_val=1, max_val=1000):
    """Menghasilkan daftar angka acak."""
    return [random.randint(min_val, max_val) for _ in range(count)]

# Judul aplikasi
st.title("📊 Cumulative Sum Calculator")
st.subheader("Perbandingan Metode Iteratif dan Rekursif")

# Deskripsi aplikasi
st.markdown("""
Aplikasi ini menghitung jumlah kumulatif dari serangkaian angka menggunakan dua metode:
- Iterative Method: Menggunakan perulangan.
- Recursive Method: Menggunakan rekursi.

Selain hasil, aplikasi ini juga membandingkan waktu eksekusi dan menampilkan grafik visual.
""")

# Input jumlah angka
st.sidebar.header("Pengaturan Input")
num_count = st.sidebar.number_input("Jumlah angka (1-5000):", min_value=1, max_value=5000, step=1)

# Tombol untuk memulai proses
if st.sidebar.button("Generate & Calculate"):
    try:
        # Validasi input
        if num_count < 1:
            st.error("Jumlah angka harus lebih besar dari 0.")
        else:
            # Generate angka acak
            numbers = generate_random_numbers(num_count)
            st.write("### 🎲 Angka yang dihasilkan")
            st.write(numbers)

            # Menyimpan waktu eksekusi untuk berbagai ukuran input
            iterative_times = []
            recursive_times = []
            input_sizes = list(range(1, num_count + 1))

            # Mengukur waktu eksekusi bertahap untuk setiap ukuran input
            for size in input_sizes:
                # Subset angka berdasarkan ukuran input
                subset_numbers = numbers[:size]

                # Iteratif
                start_time_iterative = time.time()
                cumulative_sum_iterative(subset_numbers)
                end_time_iterative = time.time()
                iterative_times.append(end_time_iterative - start_time_iterative)

                # Rekursif
                start_time_recursive = time.time()
                cumulative_sum_recursive(subset_numbers)
                end_time_recursive = time.time()
                recursive_times.append(end_time_recursive - start_time_recursive)

            # Membuat DataFrame untuk visualisasi
            df = pd.DataFrame({
                "Ukuran Input": input_sizes,
                "Waktu Iteratif (detik)": iterative_times,
                "Waktu Rekursif (detik)": recursive_times
            })

            # Konversi kolom ke float
            df["Waktu Iteratif (detik)"] = df["Waktu Iteratif (detik)"].astype(float)
            df["Waktu Rekursif (detik)"] = df["Waktu Rekursif (detik)"].astype(float)
            
            # Menampilkan grafik
            st.write("### 📈 Grafik Perbandingan Waktu Eksekusi vs Ukuran Input")
            st.line_chart(df.set_index("Ukuran Input"))

            # Menampilkan tabel data waktu eksekusi
            st.write("### 🔢 Data Waktu Eksekusi")
            st.dataframe(df)

    except RecursionError:
        st.error("Terjadi RecursionError. Cobalah dengan jumlah angka lebih kecil.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")