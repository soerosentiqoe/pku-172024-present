import streamlit as st

def app():
    st.title('Tentang Kecanduan Ponsel')

    st.write("""
    Model ini merupakan salah satu prototype untuk mengukur, memprediksi dan mengklasifikasi apakah seseorang terindikasi kecanduan gadget atau tidak.
             
    **Origin and Source:**

    * **Origin:** Kecanduan gadget merupakan salah satu sebab seseorang menjadi kurang bersosialisasi dan menghabiskan sebagian besar waktunya dengan memainkan gadget. Meskipun di sisi lain, gadget menjadi bagian yang semakin tidak terpisahkan dari kehidupan. Saat ini pun proses bekerja telah banyak bergeser dari penggunaan alat konvensional ke arah penggunaan gadget untuk penyelesaian pekerjaan.
    * **Source:** Data diperoleh dari Kagle (https://www.kaggle.com/)

    **Dataset Characteristics:**

    * **Type:** Supervised learning dataset.
    * **Features (9):**
        - `gender` : Jenis kelamin dari responden dataset.
        - `jenjangPekerjaan` : Jenis pekerjaan responden, terdiri dari Pelajar, Mahasiswa, atau Bekerja
        - `durasiPonsel` : Jumlah total lama waktu yang dihabiskan responden untuk mengakses gadget dalam 24 jam
        - `intensitasSosmed` : Ukuran indikator responden tentang intensitas aktivitas di media sosial.
        - `gangguanTidur` : Ukuran indikator intensitas yang dirasakan responden terhadap gangguan tidur akibat menggunakan gadget.
        - `cemasPonselTertinggal` : Ukuran indikator yang dirasakan responden terhadap intensitas kecemasan yang terjadi apabila gadget tertinggal/ tidak dibawa.
        - `gangguanProduktivitas` : Ukuran indikator yang dirasakan responden terhadap gangguan proditivitas (terutama dalam hal pekerjaan) akibat terlalu sering - menggunakan gadget.
        - `kecanduan` : *(Variabel Target)* Indikator apakah responden kecanduan gadget.

    **Anggota Kelompok:**
       1. Undip Y.A. Nugroho
       2. Parno
       3. Johan Muslim
       4. Haekal Baharudin Yusuf               

    
    """) 
app() 
