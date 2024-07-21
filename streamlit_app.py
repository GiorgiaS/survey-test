import streamlit as st
# import cv2
# import numpy as np

# Display Image
imagePath = ".\images\MetaversePlaza.jpeg"
st.image(imagePath)

# Set text:
text1 = 'The Metaverse is a virtual environment where people join to do different kinds of activities, like meeting with friends, playing virtual games, and participating in social events.' 
text2 = 'Generally, people access using Virtual Reality headset, from home or anywhere they are.'
st.markdown('# Title')
st.markdown('Survey description/purpose...')
st.markdown("## Metaverse")
st.markdown(text1)
st.markdown(text2)
st.markdown('## Metaverse Working Space')
st.markdown('Explain the metaverse working space')
st.markdown('## Survey')
st.markdown('We will assume that you are an employee of a software organisation called SoftOr, and you need to access the working room. Then, we will show you two different contexts and ask you to select your privacy preferences related to the data required by the working room. For the purpose of the survey, we consider the policy of a single data, namely, your body shape – i.e., since you are accessing a working environment, you will be represented by an avatar that is close to your real physical aspect.')


# st.page_link("./pages/page1.py", label="Start")
# Button for navigation
if st.button("Start"):
    # Redirect to another page
    st.switch_page("./pages/page1.py")

# pg = st.navigation([st.Page("./pages/page1.py"), st.Page("./pages/page2.py")], position="hidden",)
# pg.run()
