import streamlit as st
from PIL import Image
from multipage import MultiPage

# Import your page modules (make sure these files are in your 'pages' directory)



# Create an instance of the app 


st.title("""
Prediksi Kecanduan Ponsel
Aplikasi berbasis Web untuk memprediksi atau mengklasifikasi seseorang terindikasi terhadap kecanduan ponsel""")
img = Image.open('imgPonsel.png')
img = img.resize((250,250))
st.image(img)
import app
import about
app2 = MultiPage()
# Add all your pages 
app2.add_page("Home", app.app) # Assuming 'predict_house_price.py' is your home page
app2.add_page("About", about.app) # Assuming 'predict_house_price.py' is your home page

#app.add_page("About the Data", about.app)

# Run the app
if __name__ == "__main__":
    app2.run()