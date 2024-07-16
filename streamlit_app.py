import streamlit as st

pg = st.navigation([st.Page("./pages/page2.py")])
pg.run()

st.write("""
Hello *World*!!""")
