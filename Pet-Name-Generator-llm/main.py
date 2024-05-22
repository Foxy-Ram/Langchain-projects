import streamlit as st
import languagehelper as lh

st.header("Generate names for your pets💫")
st.markdown("##### Names will be displayed below")
st.sidebar.subheader("Enter the following:")

col1, col2 = st.sidebar.columns(2)
with col1:
    pet_name = st.text_input("PET",placeholder = "Enter pet name")
with col2:
    pet_color = st.text_input("COLOR",placeholder = "Enter pet color")
submit = st.sidebar.button("SUBMIT")

if submit:
    #Printing the pet names that are generated
    if pet_name and pet_color:
        response = lh.get_petNames(pet_name=pet_name, pet_color=pet_color)
        st.text(response.get("names"))
        st.sidebar.success("Success")
    else:
        st.sidebar.warning("Make sure to fill above")





