
import streamlit as st
import pandas as pd 
import numpy as np 
from PIL import Image
import pickle 
from sklearn.naive_bayes import GaussianNB


#Buat Judul
st.title("""
Prediksi Kecanduan Ponsel (Web Apps)
Aplikasi berbasis Web untuk memprediksi atau mengklasifikasi seseorang terindikasi terhadap kecanduan ponsel""")
img = Image.open('imgPonsel.png')
img = img.resize((250,250))
st.image(img)

st.sidebar.header('Silahkan Untuk Upload Dataset')
upload_file = st.sidebar.file_uploader('Upload file CSV Anda')
if upload_file is not None:
    inputan = pd.read_csv(upload_file)
else:
    def input_user ():
        durasiPonsel = st.slider("Durasi (Jam)", 0, 10)
        intensitasSosmed = st.selectbox("Intensitas Penggunaan Sosmed", ["Tinggi", "Sedang", "Rendah"])
        gangguanTidur = st.selectbox("Penggunaan Ponsel Menganggu Waktu Tidur Anda", ["Sering", "Terkadang", "Tidak"])
        cemasPonselTertinggal = st.selectbox("Merasa Cemas Saat Ponsel Tertinggal", ["Sering", "Terkadang", "Tidak"])
        gangguanProduktivitas = st.selectbox("Penggunaan Ponsel Menganggu Produktivitas Anda", ["Ya", "Tidak"])
        data = {'durasiPonsel' : durasiPonsel,
            'intensitasSosmed' : intensitasSosmed,
            'gangguanTidur' : gangguanTidur,
            'cemasPonselTertinggal' : cemasPonselTertinggal,
            'gangguanProduktivitas' : gangguanProduktivitas}
        fitur = pd.DataFrame(data, index=[0])
        return fitur
    inputan = input_user()

#Menggabungkan inputan dan dataset
dataPonsel_raw = pd.read_csv('dataPonsel.csv')
dataPonsels = dataPonsel_raw.drop(columns=['kecanduan'])
df = pd.concat([inputan, dataPonsels], axis=0)

#Encode Untuk fitur ordinal
encode = ['gender', 'jenjangPekerjaan','intensitasSosmed','gangguanTidur','cemasPonselTertinggal','gangguanProduktivitas']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]
df = df[:1] #ambil baris pertama (input data user)


if upload_file is not None:
    st.write(df)
else:
    st.write('Menunggu file CSV diupload, Saat ini sedang memakai sampel inputan')
    st.write(df)

load_model = pickle.load(open('modelNBC_dataPonsel.pkl', 'rb'))


#code untuk predikis
result = ''
st.subheader('Keterangan Label Kelas')
type_candu = np.array(['Ya','Tidak'])
st.write(type_candu)
#membuat tombol untuk predikis
if st.button('Test Prediksi Kecanduan Ponsel'):
    diab_prediction = load_model.predict(df)
    prediksi_prob = load_model.predict_proba(df)
    if diab_prediction[0] == 0:
        st.subheader('Probabilitas Hasil Prediksi')
        st.write(prediksi_prob)
        result = 'Waspada! Anda Cenderung Kecanduan Ponsel'
    else:
        st.subheader('Probabilitas Hasil Prediksi')
        st.write(prediksi_prob)
        result = 'Selamat! Anda Tidak Cenderung Kecanduan Ponsel'

    st.success(result)



operation = st.sidebar.selectbox("Select CRUD Operation", ["Create", "Read", "Update", "Delete"])


