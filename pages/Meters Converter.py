import streamlit as st
from number_converter.function import convertor

st.title("Meters Converter")
st.subheader("This application converters feet and inches into meters.")
st.write("Created By: Jemael E Autridge")

feet = st.number_input("Enter Feet")
inches = st.number_input("Enter Inches")

meters = convertor(feet, inches)

if st.button("Convert"):
    st.text(f"{feet} feet and {inches} inches is equal to {meters} meters ")