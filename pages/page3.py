import streamlit as st
from pages.src.IntermediatePolicy import IntermediatePolicy
from pages.src.Utilities import Utilities
from pages.src.PredefSets import PredefSets

# Hide menu
hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

# Do the computation
ip = IntermediatePolicy()
case = 1
util = st.session_state['user_utils']

with st.spinner('...I am computing...'):
    newPrp, newRet, newTP = ip.computeIntermediatePolicy(case, util)

# Print results
predSets = PredefSets()

st.markdown('''
            ## Intermediate Policy
            The resulting privacy policy for the body shape, considering your preferences, the preferences of the other users, and the space's requirements, is the following:
            ''')

st.write('Purpose:', newPrp)
prpPP = util.getprpListCase1()
prpPol = predSets.getSpacePrpCase1()
with st.expander("Extend to compare your preference with the policy"):
    # st.write('Your preference:', prpPP)
    # st.write('Policy:', prpPol)
    st.write('Your Preference:', '[', ', '.join(prpPP), ']')
    st.write('Policy:', '[', ', '.join(prpPol), ']')

st.write('Third Party:', newTP)
tpPP = util.getTpListCase1()
tpPol = predSets.getSpaceTPCase1()
with st.expander("Extend to compare your preference with the policy"):
    # st.write('Your preference:', tpPP)
    # st.write('Policy:', tpPol)
    st.write('Your Preference:', '[', ', '.join(tpPP), ']')
    st.write('Policy:', '[', ', '.join(tpPol), ']')

st.write('Retention: ', newRet)
retPP = util.getRetListCase1()
retPol = predSets.getSpaceRetCase1()
with st.expander("Extend to compare your preference with the policy"):
    st.write('Your preference:', retPP)
    st.write('Policy:', retPol)
    

st.markdown('''
            You can compare the results with the preferences of the other participants. Please note that this information is usually private, and accessing the privacy preferences of others is not allowed.
            However, for the purpose of this experiment, we want to show you why our system defines a determinate intermediate policy.
            ''')
purposes = predSets.getPrpPP(case)
with st.expander("Extend to see the purposes"):
    i = 0
    for prp in purposes:
        i += 1
        # st.write(i, prp)
        st.write(i, '[', ', '.join(prp), ']')

thirdparties = predSets.getTPPP(case)
with st.expander("Extend to see the third parties"):
    i = 0
    for tp in thirdparties:
        i += 1
        # st.write(i, tp)
        st.write(i, '[', ', '.join(tp), ']')

retentions = predSets.getRetPP(case)
with st.expander("Extend to see the retention periods"):
    i = 0
    for ret in retentions:
        i += 1
        st.write(i, ret)
        # st.write(i, '[', ', '.join(ret), ']')


# st.page_link("./pages/page2.py", label="Back")
