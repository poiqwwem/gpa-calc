import time
import numpy as np
import pandas as pd
import streamlit as st

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


placeholder = st.empty()

st.title("GPA Calculator")
st.subheader("Calculate you GPA")
classes = st.number_input(
    "How many classes are you taking?", min_value=1, max_value=10, value=3)
grades = []
for i in range(classes):
    grade = st.number_input(f"Grade for class {i + 1} (%)")
    grades.append(grade)
if st.button("Calculate GPA"):
    if len(grades) > 0:
        gpa = sum(grades) / 100 * 4
        if gpa > 4:
            gpa = 4
        st.success(f"Your GPA is {gpa:.2f}")
        if gpa > 3.9:
            st.text("Keep up the great work! 🥳")
            st.balloons()
        elif gpa > 3.2:
            st.text("Keep going, you got this!💪")
        elif gpa > 2.5:
            st.text("You got this. Keep working hard")
        elif gpa > 1.9:
            st.text("ye u might be cooked🫡")
        time.sleep(2)
        st.text("Refresh to reset")

#  streamlit run web.py
