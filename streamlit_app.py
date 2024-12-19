# Streamlit App: Cumulative Sum
import streamlit as st
import time
import random
import matplotlib.pyplot as plt
import numpy as np

def cumulative_sum_iterative(numbers):
    """Menghitung jumlah kumulatif dari array angka menggunakan iterasi dengan kompleksitas tambahan."""
    cumulative = []
    current_sum = 0
    for number in numbers:
        # Tambahkan perhitungan tambahan untuk meningkatkan kompleksitas
        for _ in range(len(numbers)):
            current_sum += 0  # Operasi dummy untuk meningkatkan waktu proses
        current_sum += number
        cumulative.append(current_sum)
    return cumulative

def cumulative_sum_recursive(numbers, index=0, current_sum=0, result=None):
    """Menghitung jumlah kumulatif dari array angka menggunakan rekursi dengan kompleksitas tambahan."""
    if result is None:
        result = []

    if index == len(numbers):  # Base case: jika index melebihi panjang array
        return result

    # Tambahkan perhitungan tambahan untuk meningkatkan kompleksitas
    for _ in range(len(numbers)):
        current_sum += 0  # Operasi dummy untuk meningkatkan waktu proses

    current_sum += numbers[index]
    result.append(current_sum)

    # Panggilan rekursif untuk elemen berikutnya
    return cumulative_sum_recursive(numbers, index + 1, current_sum, result)

def generate_random_numbers(count, min_val=1, max_val=100):
    """Menghasilkan daftar angka acak."""
    return [random.randint(min_val, max_val) for _ in range(count)]

def plot_graph(x, y_iterative, y_recursive):
    """Menampilkan grafik hasil iteratif dan rekursif."""
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_iterative, label='Iterative', marker='o', color='blue')
    plt.plot(x, y_recursive, label='Recursive', marker='x', color='green')
    plt.title('Cumulative Sum: Iterative vs Recursive')
    plt.xlabel('Index')
    plt.ylabel('Cumulative Sum')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

# Judul aplikasi
st.title("Penjumlahan Berantai (Cumulative Sum)")

# Deskripsi aplikasi
st.write("Aplikasi ini menghitung jumlah kumulatif dari serangkaian angka menggunakan algoritma iteratif dan rekursif dengan tambahan kompleksitas.")

# Input jumlah angka
num_count = st.number_input("Masukkan jumlah angka yang ingin di-generate (RNG):", min_value=1, step=1)

# Jika tombol generate ditekan
if st.button("Generate Angka dan Hitung"):
    try:
        # Generate angka secara acak
        numbers = generate_random_numbers(num_count)
        st.write(f"Angka yang dihasilkan: {numbers}")

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

        # Hitung selisih waktu
        time_difference = abs(iterative_time - recursive_time)

        # Tampilkan hasil
        st.success(f"Hasil Iteratif: {result_iterative}")
        st.write(f"Waktu Eksekusi Iteratif: {iterative_time:.6f} detik")

        st.success(f"Hasil Rekursif: {result_recursive}")
        st.write(f"Waktu Eksekusi Rekursif: {recursive_time:.6f} detik")

        st.info(f"Selisih Waktu Eksekusi: {time_difference:.6f} detik")

        # Plot grafik
        x = np.arange(1, len(numbers) + 1)
        plot_graph(x, result_iterative, result_recursive)
    except ValueError:
        st.error("Terjadi kesalahan saat menghitung jumlah kumulatif.")
