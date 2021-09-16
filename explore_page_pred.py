import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache

def load_data():
    df =pd.read_csv('car_data2.csv')

df = load_data()

def show_explore_page():
    st.title("Explore Used Car Price")

    st.write(
        """
        ### Used Car Price
        """
    )

    data = df["name"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")

    st.write("""#### Number of Used Car""")

    st.pyplot(fig1)