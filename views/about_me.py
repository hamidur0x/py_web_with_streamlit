import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()



col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_image.png", width=230)

with col2:
    st.title("Hamidur Rahman", anchor=False)
    st.write(
        "Student at Munshigonj Polytechnic Institute."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()


st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - Graphics Designer
    - programar
    - Expart in MS Application
    """
)


st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    - Programming: Python
    """
)
