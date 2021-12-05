from pandas.core.tools import numeric
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set the style for seaborn
sns.set_style('darkgrid')

# title of the app
st.title("Data Visualization App")
st.write('A car features data exploration app')

def load_data():
    """Utility function for loading car dataset as a dataframe"""
    df = pd.read_csv("C:/Users/pc/Desktop/Jenny Work/Homework/CarPrice.csv")

    return df


# load dataset
data = load_data()
numeric_columns = data.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
print(numeric_columns)

checkbox = st.sidebar.checkbox("Reveal data.")
print(checkbox)

if checkbox:
    # st.write(data)
    st.dataframe(data=data)

def main():
    st.write("Shape of the data")
    st.dataframe(data.shape)

    st.text("The number of cars in original data:" +str(len(data.index)))

    st.write("## Data Description")
    st.write("This shows different kinds of data and other statistics of our data")
    st.dataframe(data.describe())

    st.write("This shows the data type in our dataset")
    st.text(data.dtypes)

main()

# create scatterplots
st.sidebar.subheader("Scatter plot setup")

# add select widget
select_box1 = st.sidebar.selectbox(label='X axis', options=numeric_columns)
print(select_box1)
select_box2 = st.sidebar.selectbox(label='Y axis', options=numeric_columns)
print(select_box2)

# create scatterplot
sns.relplot(x=select_box1, y=select_box2, data=data)
st.pyplot(plt)

