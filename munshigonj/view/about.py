import streamlit as st

from contract.form import contact_form

@st.dialog("Contact Us")
def show_contact_form():
    contact_form()



col1, col2 = st.columns(2, gap="large", vertical_alignment="center")
with col1:
    st.image("image/campus_1.jpg")

with col2:
    st.title("Munshigonj polytechnic Institute")
    st.write("Diploma in Engineering")
    if st.button("✉️ Contact Us"):
        show_contact_form()
