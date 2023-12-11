import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("MCDA-5540: Python Assignment")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    st.success("CSV file successfully uploaded!")

    df = pd.read_csv(uploaded_file)
    required_columns = ["Name", "Age"]

    if all(col in df.columns for col in required_columns):
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.subheader("Histogram of Ages")
        plt.hist(df["Age"], bins=20, edgecolor="black")
        plt.xlabel("Age")
        plt.ylabel("Frequency")
        st.pyplot()

    else:
        st.error("The CSV file is missing one or more required columns. Please upload a valid file.")