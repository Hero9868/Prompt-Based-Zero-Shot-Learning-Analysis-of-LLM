import streamlit as st
from inference import get_generation
import constants as const


def intro():
    st.sidebar.success("Choose an option above to start.")

def option_a():
    st.code(const.TRANSPILE_PROMPT)
    click=st.button("Generate")
    if click:
        prediction = get_generation(const.TRANSPILE_PROMPT)
        st.code(prediction)


def option_b():
    st.code(const.EXPLAIN_WORD)
    click=st.button("Generate")
    if click:
        prediction = get_generation(const.EXPLAIN_WORD)
        st.code(prediction)

def option_c():
    st.code(const.CATCHY_PROMPT)
    click=st.button("Generate")
    if click:
        prediction = get_generation(const.CATCHY_PROMPT)
        st.code(prediction)
