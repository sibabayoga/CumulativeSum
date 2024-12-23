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
st.title("📊 *Cumulative Sum Calculator*")
st.subheader("Perbandingan Metode Iteratif dan Rekursif")

# Deskripsi aplikasi
st.markdown("""
Aplikasi ini menghitung *jumlah kumulatif* dari serangkaian angka menggunakan dua metode:
- *Iterative Method*: Menggunakan perulangan.
- *Recursive Method*: Menggunakan rekursi.

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

            # Hitung menggunakan iterasi
            start_time_iterative = time.time()
            result_iterative = cumulative_sum_iterative(numbers)
            end_time_iterative = time.time()
            iterative_time = end_time_iterative - start_time_iterative

            # Hitung menggunakan rekursi
            start_time_recursive = time.time()
            result_recursive = cumulative_sum_recursive(numbers)
            end_time_recursive = time.time()
            recursive_time = end_time_recursive - start_time_recursive

            # Menampilkan hasil
            st.write("### 🔢 *Hasil Perhitungan*")
            col1, col2 = st.columns(2)
            with col1:
                st.write("*Metode Iteratif*")
                st.write(result_iterative)
                st.success(f"Waktu Eksekusi: {iterative_time:.6f} detik")

            with col2:
                st.write("*Metode Rekursif*")
                st.write(result_recursive)
                st.success(f"Waktu Eksekusi: {recursive_time:.6f} detik")

            # Menampilkan perbandingan waktu
            time_difference = abs(iterative_time - recursive_time)
            st.info(f"⚡ *Selisih Waktu Eksekusi*: {time_difference:.6f} detik")

            # Visualisasi menggunakan Streamlit
            st.write("### 📈 *Visualisasi Grafik Waktu Eksekusi vs Ukuran Input*")

            # Membuat data untuk waktu eksekusi vs ukuran input
            input_sizes = [num_count]  # Ukuran input hanya 1 kali (karena kita hanya hitung waktu eksekusi untuk satu ukuran input)
            iterative_times = [iterative_time]
            recursive_times = [recursive_time]

            # Membuat DataFrame untuk visualisasi
            df = pd.DataFrame({
                "Waktu Eksekusi (detik)": iterative_times + recursive_times,
                "Ukuran Input": [num_count] * 2  # Menampilkan ukuran input yang sama untuk kedua metode
            })

            # Menampilkan grafik
            st.write("### 📈 *Grafik Perbandingan Waktu Eksekusi*")
            st.bar_chart(df.set_index("Ukuran Input"))

    except RecursionError:
        st.error("Terjadi RecursionError. Cobalah dengan jumlah angka lebih kecil.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")