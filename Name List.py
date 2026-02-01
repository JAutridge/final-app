import streamlit as st
import NameList_function as fun
nlist = fun.show()
number = ''
checkbox = ''
def add_n():
    name = st.session_state["name"]
    fun.add(name)
def clear():
    st.session_state['name'] = ""
    st.session_state['rname'] = ""

st.title("Name List")
st.subheader("This application allows you to add, edit and delete names from a list.")
st.write("Created By: Jemael E Autridge")
st.text_input(label="", placeholder="Enter New Name", on_change=add_n, key='name')
st.text_input(label="", placeholder="Enter Replacement Name", key='rname')

for num, n in enumerate(nlist):
    checkbox2 = st.checkbox(n, key=n)
    if checkbox2:
        number, checkbox = num, checkbox2

if st.button("Edit"):
    fun.replace(nlist[number], st.session_state.get('rname'))
    st.rerun()

if st.button("Delete", on_click=clear):
    fun.delete(nlist[number])
    st.rerun()

if st.button("Delete All", on_click=clear):
    fun.deleteALL()
    st.rerun()
