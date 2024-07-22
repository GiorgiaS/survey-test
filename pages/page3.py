import streamlit as st
from pages.src.IntermediatePolicy import IntermediatePolicy

# Do the computation
ip = IntermediatePolicy()
case = 1
newPrp, newRet, newTP = ip.computeIntermediatePolicy(case)

st.markdown('''
            ## Intermediate Policy  
            The resulting privacy policy for the body shape, considering your preferences, the preferences of the other users, and the space's requirements, is the following:
            ''')
st.write('Purpose:', newPrp)
st.write('Third Part:', newRet)
st.write('Retention: ', newRet)

# st.page_link("./pages/page2.py", label="Back")
