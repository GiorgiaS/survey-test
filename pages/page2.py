import streamlit as st
from pages.src.Utilities import Utilities
from pages.src.PredefSets import PredefSets

predSets = PredefSets()
util = Utilities()

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

purposes = predSets.getSpacePrpCase1()
st.markdown('Purpose (select at leasto one):')
prpList = []
for prp in purposes:
        selectedPrp = st.checkbox(prp)
        if selectedPrp:
                prpList.append(prp)

util.setprpListCase1(prpList)
        
thyrdparties = ['Newsletter/Marketing', 'Project/Task management', 'Web analytics', 'Virtual meetings/events', 'Cloud computing service']
st.markdown('Third parties (select at least one):')
tpList = []
for tp in thyrdparties:
        selectedTP = st.checkbox(tp)
        if selectedTP:
                tpList.append(tp)
util.setTpListCase1(tpList)

retention = predSets.getSpaceRetCase1() #days
st.markdown('Retention period:')
selRet = st.slider("Retention", 1, retention, retention//2, label_visibility='collapsed')
util.setRetCase1(selRet)

# Button for navigation
columns = st.columns((2, 1, 2))
buttonStart = columns[1].button('Next')
if buttonStart:
    # Redirect to another page
    st.switch_page("./pages/page3.py")

