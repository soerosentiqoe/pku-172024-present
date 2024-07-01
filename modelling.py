import streamlit as st

def app():
    #st.title("Model Selection and Performance")

    st.write("""
    ## Building Machine Learning Models

    Tujuan dari modelling ini adalah untuk memprediksi apakah seseorang kecanduan ponsel atau tidak berdasarkan beberapa parameter.  Langkah yang kami lakukan:

    **1. Data Preparation:**

    * **Loading:**  Import dataset dataponselnew.csv.
    * **Exploration (EDA):** Melakukan analisa terhadap feature yang tersedia.
    
    **2. Train-Test Split:**

    * Melakukan split dataset untuk **training set** (80%) dan **testing set** (20%).
    
    **3. Model Selection and Training:**

    Kami melakukan percobaan dengan beberapa model, yaitu:

    * **SVM** 
    * **Decision Tree** 
    * **Random Forest** 
    * **XGBoost** 
    
    **4. Model Evaluation (K-Fold Cross Validation):**

    Kami menggunakan K-Fold Cross Validation untuk menentukan model terbaik.

    ## Results:

    | Model             | Train    | Test     |
    |-------------------|----------|----------|
    | SVM               | 1.000000 | 0.806085 |
    | Decision Tree     | 1.000000 | 0.806085 |
    | Random Forest     | 0.997900 | 0.902028 |
    | XGBoost           | 1.000000 | 0.884921 |

    ## Analysis:

    * **Best Model:** Random Forest, dengan nilai test accuracy terbesar.
    
    """)
app() 
