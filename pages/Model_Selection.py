import streamlit as st
import pandas as pd
df=pd.read_csv('./dataponselnew.csv')
x=pd.read_csv('./assets/x.csv')
df = df.drop('Unnamed: 0', axis=1)
x = x.drop('Unnamed: 0', axis=1)

import base64

# Function to load image and convert to base64 string
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode()
    return base64_image

# Load your image
image_path = "imgPonsel.png"  # Replace with the path to your image
base64_image = get_base64_image(image_path)

# Create a title with image and text
html_title = f"""
<div style="display: flex; align-items: center;">
    <img src="data:image/png;base64,{base64_image}" style="width:50px; height:50px; margin-right:10px;">
    <h1 style="display: inline;">Prediksi Kecanduan Ponsel</h1>
   
</div>
 <span>Aplikasi berbasis Web untuk memprediksi atau mengklasifikasi seseorang terindikasi terhadap kecanduan ponsel.</span>
"""

st.set_page_config(
    page_title="Prediksi Kecanduan HP",
    page_icon="assets/DC.png",  # Path to your icon file
)

def app():
    st.title("Model Selection and Performance")

    st.write("""
    ## Building Machine Learning Models

    Tujuan dari modelling ini adalah untuk memprediksi apakah seseorang kecanduan ponsel atau tidak berdasarkan beberapa parameter.  Langkah yang kami lakukan:

    **1. Data Preparation:**

    * **Loading:**  Import dataset dataponselnew.csv.
    * **Exploration (EDA):** Melakukan analisa terhadap feature yang tersedia.** """)
             

    st.write("""**2. One Hot Encoding:**

    * mengubah kategorikal column.""")
    st.dataframe(df.head())
    st.write("menjadi")
    st.dataframe(x.head())
    
    st.write(""" **3. Train-Test Split:**

    * Melakukan split dataset untuk **training set** (80%) dan **testing set** (20%).
    
    **4. Model Selection and Training:**

    Kami melakukan percobaan dengan beberapa model, yaitu:

    * **SVM** 
    * **Decision Tree** 
    * **Random Forest** 
    * **XGBoost** 
    
    **5. Model Evaluation (K-Fold Cross Validation):**

    Kami menggunakan K-Fold Cross Validation untuk menentukan model terbaik.

    ## Results:

   * **RF Train     0.967612**
    * **RF Test      0.879894**
    * **XG Train     0.956233**
    * **XG Test      0.872487**
    * **DT Train     0.969362**
    * **DT Test      0.828131**
    * **SVM Train    0.969362**
    * **SVM Test     0.828131**

    ## Analysis:

    * **Best Model:** Random Forest, dengan nilai test accuracy terbesar.
    
    """)
    st.image('./assets/1.png')
    st.subheader('Feature Importance :')
    st.image('./assets/2.png')
app() 
