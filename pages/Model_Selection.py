import streamlit as st
import pandas as pd
df=pd.read_csv('./dataponselnew.csv')
x=pd.read_csv('./assets/x.csv')
df = df.drop('Unnamed: 0', axis=1)
x = x.drop('Unnamed: 0', axis=1)
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
