# Streamlit App: Cumulative Sum
import streamlit as st
import time

def cumulative_sum_iterative(numbers):
    """Menghitung jumlah kumulatif dari array angka menggunakan iterasi."""
    cumulative = []
    current_sum = 0
    for number in numbers:
        current_sum += number
        cumulative.append(current_sum)
    return cumulative

def cumulative_sum_recursive(numbers, index=0, current_sum=0, result=None):
    """Menghitung jumlah kumulatif dari array angka menggunakan rekursi."""
    if result is None:
        result = []

    if index == len(numbers):  # Base case: jika index melebihi panjang array
        return result

    current_sum += numbers[index]
    result.append(current_sum)

    # Panggilan rekursif untuk elemen berikutnya
    return cumulative_sum_recursive(numbers, index + 1, current_sum, result)

# Judul aplikasi
st.title("Penjumlahan Berantai (Cumulative Sum)")

# Deskripsi aplikasi
st.write("Aplikasi ini menghitung jumlah kumulatif dari serangkaian angka menggunakan algoritma iteratif dan rekursif.")

# Input dari pengguna
numbers_input = st.text_input("Masukkan angka, dipisahkan dengan koma (contoh: 1,2,3,4,5):")

# Jika tombol hitung ditekan
if st.button("Hitung"):
    try:
        # Konversi input menjadi daftar angka
        numbers = list(map(int, numbers_input.split(',')))

        # Hitung menggunakan iterasi
        start_time_iterative = time.time()
        result_iterative = cumulative_sum_iterative(numbers)
        end_time_iterative = time.time()

        # Hitung menggunakan rekursi
        start_time_recursive = time.time()
        result_recursive = cumulative_sum_recursive(numbers)
        end_time_recursive = time.time()

        # Tampilkan hasil
        st.success(f"Hasil Iteratif: {result_iterative}")
        st.write(f"Waktu Eksekusi Iteratif: {end_time_iterative - start_time_iterative:.6f} detik")

        st.success(f"Hasil Rekursif: {result_recursive}")
        st.write(f"Waktu Eksekusi Rekursif: {end_time_recursive - start_time_recursive:.6f} detik")
    except ValueError:
        st.error("Pastikan Anda hanya memasukkan angka yang dipisahkan dengan koma.")
