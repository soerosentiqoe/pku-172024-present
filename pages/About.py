import streamlit as st
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('./dataponselnew.csv')
df=df.drop('Unnamed: 0', axis=1)
def app():
    st.title('Tentang Dataset Cellphone Addiction')

    st.write("""
    Data ini menampilkan hasil survey sekitar 500 responden mengenai kesehariannya dalam menggunakan telepon seluler.

    **Source: kaggle.com**

    **Dataset Characteristics:**

    * **Type:** Supervised learning dataset for regression (predicting a continuous target variable).
    * **Instances:** 512 responden.
    * **Features (9):**
        - `gender`: Jenis Kelamin.
        - `jenjangPekerjaan`: Pekerjaan responden.
        - `durasiPonsel`: durasi penggunaan ponsel (jam) dalam sehari.
        - `intensitasSosmed`: intensitas penggunaan ponsel untuk sosial media.
        - `gangguanTidur`: intesitas mengalami gangguan tidur.
        - `cemasPonselTertinggal`: intensitas rasa cemas ketika ponsel tertinggal.
        - `gangguanProduktivitas`: gangguan produktivitas.
        - `kecanduan`: Target variable.
    """)    
    st.header("Data")
    # Display the DataFrame as a table
    st.dataframe(df)
    st.header("EDA")
    # Select columns to plot
    x_axis = st.selectbox('Select the column for the X axis', df.columns)
    y_axis = st.selectbox('Select the column for the Y axis', df.columns,index=7)

    agg_func = st.selectbox('Select aggregation function', ['sum', 'mean', 'max', 'min'])
    # Select plot dimensions
    plot_width = st.number_input('Plot width (inches)', min_value=1, max_value=100, value=8)
    plot_height = st.number_input('Plot height (inches)', min_value=1, max_value=100, value=30)

    # Aggregate the DataFrame
    if x_axis and y_axis:
        if agg_func == 'sum':
            aggregated_df = df.groupby(x_axis)[y_axis].sum().reset_index()
        elif agg_func == 'mean':
            aggregated_df = df.groupby(x_axis)[y_axis].mean().reset_index()
        elif agg_func == 'max':
            aggregated_df = df.groupby(x_axis)[y_axis].max().reset_index()
        elif agg_func == 'min':
            aggregated_df = df.groupby(x_axis)[y_axis].min().reset_index()

        # Plotting
        value_counts = df[x_axis].value_counts()

        # Display value counts as a bar plot in Streamlit
        st.bar_chart(value_counts,x_label=x_axis, y_label=y_axis)
        #fig, ax = plt.subplots(figsize=(plot_width, plot_height))
        
        #ax.bar(aggregated_df[x_axis], aggregated_df[y_axis])
        #ax.bar(aggregated_df[x_axis], aggregated_df[y_axis])
        #ax.set_xlabel(x_axis)
        #ax.set_ylabel(f'{agg_func.capitalize()} of {y_axis}')
        #ax.set_title(f'{agg_func.capitalize()} of {y_axis} by {x_axis}')
        #st.pyplot(fig)
        #st.bar_chart(aggregated_df[x_axis], aggregated_df[y_axis])
        #st.bokeh_chart(fig)

app() 
