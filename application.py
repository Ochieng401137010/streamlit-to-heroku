from numpy import select
import streamlit as st
import plotly_express as px
import pandas as pd
import numpy as np

# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)

# title of the app
st.title("Data Visualization App")

# Add a sidebar
st.sidebar.subheader("Visualization Settings")

# Setup file upload
uploaded_file = st.sidebar.file_uploader(label="Upload your CSV or Excel file.", type=['csv', 'xlsx'])

global df
if uploaded_file is not None:
    print(uploaded_file)
    print("hello")
    
    try: 
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_csv(uploaded_file)

global numeric_columns
try:
    st.write(df)
    numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
except Exception as e:
    print(e)
    str.write("Please upload file to the application.")

st.write(df)

# add a select widget to the side bar
chart_select = st.sidebar.selectbox(
    label="Select the chart type",
    options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
)

if chart_select == 'Scatterplots':
    st.sidebar.subheader("Scatterplot Settings")
    try:
        x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values)
        # display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

else:
    chart_select == 'Lineplots':
    st.sidebar.subheader("Lineplots Settings")
    try:
        x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
        plot = px.lineplot(data_frame=df, x=x_values, y=y_values)
        # display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)



