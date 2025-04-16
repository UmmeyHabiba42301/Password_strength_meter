import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")

st.title("Password Strength Meter")
st.markdown(""""
Welcome to the password strength meter!👋
use this simple tool to check the strength of your password and get suggestion on hoe to make it stronger.
we will give you a helpful tips to create a **strong password**🔐""")

password  = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else :
        feedback.append("❌Password should be atleast 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌Password should contain both upper and lower case characters.")

    if re.search(r'[0-9]', password):
        score +=1
    else :
        feedback.append("❌Password should contain atleast one digit.")

    if re.search(r'[!@#$*&+-=]' , password):
        score += 1
    else:
        feedback.append("❌Password should atleast contain one special characters(!@#$*&+-=).")
    if score == 4:
        feedback.append("✅Your Password is Strong!")
    elif score ==3:
        feedback.append("⭐Your Password is Medium strength.It could be stronger")
    else:
        feedback.append("🔴Your Password is weak.Please make it stronger.")

    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
          st.write(tip)
else:
    st.info("Please enter your Password to get started.")