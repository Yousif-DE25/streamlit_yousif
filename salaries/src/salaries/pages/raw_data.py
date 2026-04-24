import streamlit as st
from salaries.utils.constants import get_salaries_df

def raw_data():
    st.markdown("# RAW DATA")
    st.dataframe(get_salaries_df())

if __name__ == "__main__":
    raw_data()
