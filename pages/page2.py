import streamlit as st

# st.write("""
# Hello *World*""")
st.markdown("## Scenario 1:")
st.markdown('Imagine you need to access SoftOrg\'s metaverse workspace to meet with representatives from a key client factory. Your manager and three colleagues will also be attending the meeting. In total, there will be five *SoftOrg* employees, including yourself, and two customer representatives connected to the virtual space.')
st.markdown('''You and other participants must share, among others, data related to your physical aspect (i.e., the body shape) to access the virtual working space.  
        The policy defined by the space related to the physical body is the following:  
        :star: Purpose = {Basic service, Analytics/Research, Marketing, Legal requirement, Service operation and security, Additional service/feature}  
        :star: Retention = 90 day  
        :star: Third party = {Newsletter/Marketing, Project/Task management, Web analytics, Virtual meetings/events, Cloud computing service}  
        ''')
# Eg of third parties:
# https://www.convert.com/list-of-third-parties-with-whom-we-share-data/
# :star: Third party = {Active Campaign, Asana, Google Analytics, Google Meet, AWS}  

with st.expander("See policy definition"):
        st.markdown('''
                    **Purpose:** for which purpose data are collected by the metaverse working space. For instance, the physical aspectt is collected to provide the basic service.  
                    **Retention:** how long data is maintained. After this period, data is removed from databases. For instance, the physical aspect is retained for 90 days.  
                    **Third party:** to which parties external to the working space data are shared. For instance, the physical aspect is shared with third party emailing newsletter and marketing.  
                    ''')       

st.markdown('''
            Given the defined policy, select your privacy preferences staing to which extent do you want to share your physical body information.
            ''')
purposes = ['Basic service', 'Analytics/Research', 'Marketing', 'Legal requirement', 'Service operation and security', 'Additional service/feature']
selectedPrp = st.checkbox('Purpose (select at leasto one):', purposes)
st.write('You selected:', selectedPrp)


# Button for navigation
columns = st.columns((2, 1, 2))
buttonStart = columns[1].button('Next')
if buttonStart:
    # Redirect to another page
    st.switch_page("./pages/page3.py")
