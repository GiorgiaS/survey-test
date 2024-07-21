import streamlit as st

# st.write("""
# Hello *World*""")
st.markdown("## Scenario 1:")
st.markdown('Imagine you need to access SoftOrg\'s metaverse workspace to meet with representatives from a key client factory. Your manager and three colleagues will also be attending the meeting. In total, there will be five *SoftOrg* employees, including yourself, and two customer representatives connected to the virtual space.')
st.markdown('''You and other participants must share, among others, data related to your physical aspect (i.e., the body shape) to access the virtual working space.  
        The policy is the following:  
        - Purpose = {Prp1, ….}
        <sub> I,e., for which purpose data are collected by the metaverse working space. <\sub>  
        - Retention = 90 day
        <sub> I.e., time after which data are removed <\sub>  
        - Third party = {tp1, ...}
        <sub> I.e., to which parties external to the metaverse working space data are shared <\sub>
        ''')


st.page_link("./pages/page3.py", label="Next")
