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
def cumulative_sum_recursive(numbers):
    """Menghitung jumlah kumulatif dari array angka menggunakan rekursi."""
    if numbers == []:  # Base case
        return []
    
    if numbers[1:] == []:  # Base case untuk 1 elemen
        return [numbers[0]]
        
    # Recursive case
    small_sum = cumulative_sum_recursive(numbers[:-1])  # Rekursif untuk array tanpa elemen terakhir
    return small_sum + [small_sum[-1] + numbers[-1]]  # Tambahkan hasil kumulatif terakhir

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

            # Total waktu eksekusi
            total_iterative_time = sum(iterative_times)
            total_recursive_time = sum(recursive_times)

            # Membuat DataFrame untuk visualisasi
            df = pd.DataFrame({
                "Ukuran Input": input_sizes,
                "Waktu Iteratif (detik)": iterative_times,
                "Waktu Rekursif (detik)": recursive_times
            })

            # Menampilkan grafik
            st.write("### 📈 Grafik Perbandingan Waktu Eksekusi vs Ukuran Input")
            st.line_chart(df.set_index("Ukuran Input"))

            # Menampilkan tabel data waktu eksekusi
            st.write("### 🔢 Data Waktu Eksekusi")
            st.dataframe(df)

            # Menampilkan total waktu eksekusi
            st.write("### 🕒 Total Waktu Eksekusi")
            col1, col2 = st.columns(2)
            with col1:
                st.write("*Metode Iteratif*")
                st.success(f"Total Waktu: {total_iterative_time:.6f} detik")

            with col2:
                st.write("*Metode Rekursif*")
                st.success(f"Total Waktu: {total_recursive_time:.6f} detik")

    except RecursionError:
        st.error("Terjadi RecursionError. Cobalah dengan jumlah angka lebih kecil.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")