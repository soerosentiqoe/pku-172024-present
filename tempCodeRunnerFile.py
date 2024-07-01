
# import streamlit as st
# import pandas as pd 
# import numpy as np 
# import pickle 
# from sklearn.naive_bayes import GaussianNB


# #Buat Judul
# st.title('Data Mining Kecanduan Ponsel')


# def input_user ():
#     durasi = st.slider("Durasi (Jam)", 0, 10)
#     intensitas = st.selectbox("Intensitas Penggunaan Sosmed", ["Tinggi", "Sedang", "Rendah"])
#     tidur = st.selectbox("Penggunaan Ponsel Menganggu Waktu Tidur Anda", ["Sering", "Terkadang", "Tidak"])
#     cemas = st.selectbox("Merasa Cemas Saat Ponsel Tertinggal", ["Sering", "Terkadang", "Tidak"])
#     produktivitas = st.selectbox("Penggunaan Ponsel Menganggu Produktivitas Anda", ["Ya", "Tidak"])
#     data = {'durasi_jam' : durasi,
#             'intensitas_rg' : intensitas,
#             'tidur_rg' : tidur,
#             'cemas_rg' : cemas,
#             'produktivitas_rg' : produktivitas}

#     fitur = pd.DataFrame(data, index=[0])
# inputan = input_user()

# #Menggabungkan inputan dan dataset
# dataPonsel_raw = pd.read_csv('dataPonsel.csv')
# dataPonsels = dataPonsel_raw.drop(columns=['kecanduan'])
# df = pd.concat([inputan, dataPonsels], axis=0)

# #Encode Untuk fitur ordinal
# encode = ['gender', 'jenjangPekerjaan','intensitasSosmed','gangguanTidur','cemasPonselTertinggal','gangguanProduktivitas']
# for col in encode:
#     dummy = pd.get_dummies(df[col], prefix=col)
#     df = pd.concat([df,dummy], axis=1)
#     del df[col]
# df = df[:1] #ambil baris pertama (input data user)




# load_model = pickle.load(open('modelNBC_dataPonsel.pkl', 'rb'))
# # prediction = load_model.predict(df)

# #code untuk predikis
# result = ''

# #membuat tombol untuk predikis
# if st.button('Test Predikis Kecanduan Ponsel'):
#     diab_prediction = load_model.predict([[durasi,intensitas,tidur,cemas,produktivitas]])
#     if diab_prediction[0] == 0:
#         result = 'Cenderung Kecanduan'
#     else:
#         result = 'Tidak Cenderung Kecanduan'

#     st.success(result)