import streamlit as st
import pandas as pd

st.set_page_config(page_title="Asisten PJOK Digital", layout="centered")

st.title("🏃‍♂️ Asisten PJOK Digital: Presensi & Nilai")
st.caption("Aplikasi Web Mobile-Responsive untuk Guru SD (Kelas 4, 5, 6)")

# Navigasi Sidebar yang pas di layar HP
st.sidebar.header("⚙️ Pengaturan")
pilihan_kelas = st.sidebar.selectbox("Pilih Kelas:", ["Kelas IV", "Kelas V", "Kelas VI"])
pilihan_fitur = st.sidebar.radio("Pilih Administrasi:", ["📊 Daftar Hadir (Presensi)", "💯 Daftar Nilai Formatif/Sumatif"])

# Basis Data Siswa Utama
siswa_list = ["Ahmad Fauzi", "Budi Santoso", "Citra Lestari", "Dedi Wijaya", "Eka Putri"]

if pilihan_fitur == "📊 Daftar Hadir (Presensi)":
    st.header(f"📅 Presensi Lapangan - {pilihan_kelas}")
    pertemuan = st.selectbox("Pilih Pertemuan:", [f"Pertemuan {i}" for i in range(1, 19)])
    st.info("💡 Ketuk status kehadiran siswa langsung dari smartphone Anda.")
    
    with st.form("form_presensi"):
        for nama in siswa_list:
            col1, col2 = st.columns([2, 2])
            with col1:
                st.write(f"**{nama}**")
            with col2:
                st.radio(f"Status {nama}", ["Hadir (H)", "Sakit (S)", "Izin (I)", "Alpa (A)"], key=f"abs_{nama}", horizontal=True, label_visibility="collapsed")
        st.form_submit_button("💾 Simpan Presensi")

else:
    st.header(f"💯 Input Nilai - {pilihan_kelas}")
    pilihan_bab = st.selectbox("Pilih Bab Materi:", ["BAB 1: Waktunya Bergerak", "BAB 2: Saatnya Bermain", "BAB 3: Memadukan Gerak"])
    
    with st.form("form_nilai"):
        for nama in siswa_list:
            st.write(f"👤 **{nama}**")
            col1, col2, col3 = st.columns(3)
            f1 = col1.number_input("Formatif 1", min_value=0, max_value=100, value=80, key=f"f1_{nama}")
            f2 = col2.number_input("Formatif 2", min_value=0, max_value=100, value=80, key=f"f2_{nama}")
            s1 = col3.number_input("Sumatif", min_value=0, max_value=100, value=80, key=f"s1_{nama}")
            st.write("---")
        st.form_submit_button("💾 Simpan Semua Nilai Bab")