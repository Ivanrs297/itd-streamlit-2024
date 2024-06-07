import streamlit as st
import pandas as pd

st.header("Hola mundo")
st.title("La clase la de Ivan es la mejor")
st.markdown("**holaaaa**")

df = pd.read_csv("data.csv")
st.write("hola")
st.dataframe(df)
