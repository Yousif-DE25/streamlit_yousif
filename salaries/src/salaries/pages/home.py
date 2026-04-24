import streamlit as st
from salaries.utils.constants import IMAGES_PATH, MARKDOWN_PATH
from salaries.utils.constants import read_textfile

st.markdown("# HOME")

def home():
    st.markdown("# RAW_DATA")
    st.image(IMAGES_PATH / "salaries_data_engineering.png")
    st.markdown(read_textfile(MARKDOWN_PATH / "intro_salaries.md"))

if __name__ == "__main__":
    home()
