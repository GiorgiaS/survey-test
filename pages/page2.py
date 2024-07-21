import streamlit as st

# st.write("""
# Hello *World*""")
st.markdown("## Scenario 1:")
st.markdown('Imagine you need to access SoftOrg\'s metaverse workspace to meet with representatives from a key client factory. Your manager and three colleagues will also be attending the meeting. In total, there will be five *SoftOrg* employees, including yourself, and two customer representatives connected to the virtual space.')
st.markdown('''You and other participants must share, among others, data related to your physical aspect (i.e., the body shape) to access the virtual working space.  
        The policy defined by the space related to the physical body is the following:  
        :star: Purpose = {Prp1, ...}  
        :star: Retention = 90 day  
        :star: Third party = {tp1, ...}  
        ''')
with st.expander("See policy definition"):
        st.markdown('''
                    **Purpose:** for which purpose data are collected by the metaverse working space.  
                    **Retention:** how long data is maintained. After this period, data is removed from databases.  
                    **Third party:** to which parties external to the working space data are shared.  
                    ''')

# Button for navigation
columns = st.columns((2, 1, 2))
buttonStart = columns[1].button('Next')
if buttonStart:
    # Redirect to another page
    st.switch_page("./pages/page3.py")
