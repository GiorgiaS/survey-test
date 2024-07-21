import streamlit as st

# st.write("""
# Hello *World*""")
st.write("## Scenario 1:")
st.write('Imagine you need to access SoftOrg\'s metaverse workspace to meet with representatives from a key client factory. Your manager and three colleagues will also be attending the meeting. In total, there will be five *SoftOrg* employees, including yourself, and two customer representatives connected to the virtual space.')
st.write('''You and other participants must share, among others, data related to your physical aspect (i.e., the body shape) to access the virtual working space. 
        The policy is the following:
        - Purpose = {Prp1, ….}
        ######### I,e., for which purpose data are collected by the metaverse working space.
        - Retention = 90 day
        ######### I.e., time after which data are removed
        - Third party = {tp1, ...}
        ######### I.e., to which parties external to the metaverse working space data are shared
        ''')


st.page_link("./pages/page2.py", label="Next")
