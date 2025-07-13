import streamlit as st
import numpy as np

def hitung_ketidakpastian_gabungan(berat, ketidakpastian):
    # Menghitung ketidakpastian gabungan dengan rumus:
    # U_gabungan = sqrt(sum(U_i^2))
    ketidakpastian_gabungan = np.sqrt(np.sum(np.array(ketidakpastian) ** 2))
    return ketidakpastian_gabungan

def main():
    st.title("Pengukuran Ketidakpastian Berat")

    st.write("Aplikasi ini menghitung ketidakpastian gabungan dari pengukuran berat.")

    # Input untuk jumlah berat
    jumlah_berat = st.number_input("Masukkan jumlah berat:", min_value=1, value=1, step=1)
    
    daftar_berat = []
    daftar_ketidakpastian = []

    for i in range(jumlah_berat):
        berat = st.number_input(f"Berat {i + 1} (kg):", format="%.2f")
        ketidakpastian = st.number_input(f"Ketidakpastian untuk Berat {i + 1} (kg):", format="%.2f")
        daftar_berat.append(berat)
        daftar_ketidakpastian.append(ketidakpastian)

    if st.button("Hitung Ketidakpastian Gabungan"):
        ketidakpastian_gabungan = hitung_ketidakpastian_gabungan(daftar_berat, daftar_ketidakpastian)
        st.write(f"Ketidakpastian Gabungan: {ketidakpastian_gabungan:.4f} kg")

        # Menampilkan tabel hasil
        st.subheader("Ringkasan Pengukuran")
        data = {
            "Berat (kg)": daftar_berat,
            "Ketidakpastian (kg)": daftar_ketidakpastian
        }
        st.table(data)

if __name__ == "__main__":
    main()
