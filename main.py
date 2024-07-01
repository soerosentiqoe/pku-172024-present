import streamlit as st
from PIL import Image
from multipage import MultiPage

# Import your page modules (make sure these files are in your 'pages' directory)
from pages import Prediksi_Kecanduan_Ponsel 
from pages import Model_Selection
from pages import About

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("""
Prediksi Kecanduan Ponsel
Aplikasi berbasis Web untuk memprediksi atau mengklasifikasi seseorang terindikasi terhadap kecanduan ponsel.""")
img = Image.open('imgPonsel.png')
img = img.resize((250,250))
left_co, cent_co, right_co = st.columns(3)
with cent_co:
    st.image(img)
st.video("https://youtu.be/ajjMJABRJzE?si=1pFFeMFjsBYCS-lt")
# Add all your pages 
app.add_page("Home", Prediksi_Kecanduan_Ponsel.app)
app.add_page("About", About.app)
app.add_page("Model Explanation", Model_Selection.app)

# Run the app
if __name__ == "__Home__":
    app.run()