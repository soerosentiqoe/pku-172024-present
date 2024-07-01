import streamlit as st

def app():
    st.title("Model Selection and Performance")

    st.write("""
    ## Building Machine Learning Models

    Tujuan dari modelling ini adalah untuk memprediksi apakah seseorang kecanduan ponsel atau tidak berdasarkan beberapa parameter.  Langkah yang kami lakukan:

    **1. Data Preparation:**

    * **Loading:**  Import dataset dataponselnew.csv.
    * **Exploration (EDA):** Melakukan analisa terhadap feature yang tersedia.**
             

    **2. One Hot Encoding:**

    * mengubah kategorikal column.
    
    
    **3. Train-Test Split:**

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
