import streamlit as st
from PIL import Image
from multipage import MultiPage

# Import your page modules (make sure these files are in your 'pages' directory)
from pages import Prediksi_Kecanduan_Ponsel 
from pages import Model_Selection
from pages import About

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
# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.markdown(html_title, unsafe_allow_html=True)

#st.title("""
#Prediksi Kecanduan Ponsel
#Aplikasi berbasis Web untuk memprediksi atau mengklasifikasi seseorang terindikasi terhadap kecanduan ponsel.""")
#img = Image.open('imgPonsel.png')
#img = img.resize((250,250))
#left_co, cent_co, right_co = st.columns(3)
#with cent_co:
#    st.image(img)
st.video("https://youtu.be/ajjMJABRJzE?si=1pFFeMFjsBYCS-lt")
# Add all your pages 
app.add_page("Home", Prediksi_Kecanduan_Ponsel.app)
app.add_page("About", About.app)
app.add_page("Model Explanation", Model_Selection.app)

st.write("""
In today's digital age, cell phone addiction among kids has become a growing concern. The excessive use of mobile devices can lead to various negative effects on children's physical and mental health, academic performance, and social skills. This app aims to raise awareness about the issue and provide useful information and resources for parents and educators to help manage and mitigate cell phone addiction in kids.
""")

# Create a header for the signs and symptoms section
st.header("Signs and Symptoms of Cell Phone Addiction")

# Add content to the signs and symptoms section
st.write("""
Parents and educators should be aware of the common signs and symptoms of cell phone addiction in kids, including:
- Increased screen time and difficulty limiting use
- Irritability or anxiety when the phone is taken away
- Decline in academic performance
- Neglect of other activities and responsibilities
- Sleep disturbances due to late-night phone use
- Physical symptoms such as eye strain and headaches
""")

# Create a header for the prevention and management section
st.header("Prevention and Management Strategies")

# Add content to the prevention and management section
st.write("""
Here are some strategies to help prevent and manage cell phone addiction in kids:
- Set clear boundaries and rules for phone use
- Encourage alternative activities such as outdoor play, reading, and hobbies
- Model healthy phone use behavior as parents and educators
- Use apps and tools to monitor and limit screen time
- Communicate openly with kids about the risks of excessive phone use
- Seek professional help if necessary
""")



# Run the app
if __name__ == "__Home__":
    app.run()