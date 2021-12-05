from io import BytesIO
import streamlit as st
import plotly_express as px
import altair as alt
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

import math

# title of the app
st.title('Data Visualization App')
st.write('A car features data exploration app')

# Add a sidebar
st.sidebar.subheader("Visualization Settings")

def main():
    #data_file = st.file_uploader("Upload CSV", type=["csv"])
    #if data_file is not None:
        #st.write(type(data_file))
        #file_details = {"filename":data_file.name, "filetype":data_file.type, "filesize":data_file.size}
        #st.write(file_details)

        #st.write("Original Dataset")
    df = pd.read_csv("C:/Users/pc/Desktop/Jenny Work/Homework/CarPrice.csv")
    st.sidebar.df
    st.dataframe(df)

    st.write("Shape of the data")
    st.dataframe(df.shape)

    st.text("The number of cars in original data:" +str(len(df.index)))

    st.write("## Data Description")
    st.write("This shows different kinds of data and other statistics of our data")
    st.dataframe(df.describe())

    st.write("This shows the data type in our dataset")
    st.text(df.dtypes)

    # add a select widget to the side bar
    # chart_select = st.sidebar.selectbox(
    #     label="Select the chart type",
    #     options=['Scatterplots',  'Lineplots', 'Histogram', 'Boxplot]
    # )

main()
