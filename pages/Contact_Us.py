import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form("emailForm"):
    userEmail = st.text_input("Your email address: ")
    raw_message = st.text_area("Your message: ")
    message = f"""
    Subject: New email from {userEmail}
    
    From: {userEmail}
    {raw_message}
    """
    userSubmit = st.form_submit_button("Submit")
    if userSubmit:
        send_email(message)
        st.info("Your email was sent successfully!")
