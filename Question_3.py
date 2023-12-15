import streamlit as st
import pandas as pd
import plotly.express as px

# Set the title of the app
st.title("CSV File Uploader")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(uploaded_file)

    # Plot histogram of ages using Plotly Express
    fig = px.histogram(df, x="Age", nbins=20)
    st.plotly_chart(fig)