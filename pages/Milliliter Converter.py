import streamlit as st
from number_converter.function2 import convertor2

st.title("Milliliter Converter")
st.subheader("This application converters ounces into milliliters.")
st.write("Created By: Jemael E Autridge")

ounces = st.number_input("Enter Ounces")
milliliters = convertor2(ounces)

if st.button("Convert"):
    st.text(f"{ounces} Ounces is equal to {milliliters} milliliters ")