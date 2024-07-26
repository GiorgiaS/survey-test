import streamlit as st
import cv2
import numpy as np

def set_page_config():
    """Sets the page configuration.
    """
    st.set_page_config(
        page_title="Privacy-Preserving Metaverse",
        layout="wide",
    )
set_page_config()

# Hide menu
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
        #GithubIcon {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
        #stSidebarNav {display: none;}
        #root > div:nth-child(1) > div.withScreencast > div > div > header > div.st-emotion-cache-15ecox0.ezrtsby0 > div > div:nth-child(3) {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


# Make the app take up all the available space in the browser window and not just a single column
# st.set_page_config(layout='wide')

# st.title('Privacy-Preserving Metaverse')

# Display Image
imagePath = "./images/MetaversePlaza.jpeg"
st.image(imagePath)

# Set text:
st.markdown('## Privacy in the Metaverse')
st.markdown("### Metaverse")
st.markdown('The Metaverse is a dynamic virtual environment where people engage in various activities, such as meeting friends, playing games, and attending social events. This immersive world is typically accessed using a virtual reality headset, allowing users to connect from the comfort of their homes or any location. The Metaverse is rapidly evolving, offering endless possibilities for interaction, entertainment, and even work.')
st.markdown('### Survey')
st.markdown('Let us assume you are a metaverse user and need access to a space with other people where you must share your personal data with them. This data consists of the requirements of the specific virtual space, which are specified through policies.')
st.markdown('*Would you share all the required data? To which extend would you agree with the policies?*')
st.markdown('We aim to create a system that respects everyone\'s privacy. This system will manage and balance the privacy preferences of all participants, including yours, along with the requirements of the shared space. In this survey, we will present two scenarios in the metaverse where you will set your privacy preferences. We will then integrate your choices with those of other users and the space\'s policies. Finally, we will ask you a few questions about how you feel about the new policy.')
st.markdown('### Scenario: Metaverse Working Space')
st.markdown('A metaverse working space (like Meetaverse) is a virtual 3D room where people can join to collaborate, organise meetings, and work together. The working room has some requirements to improve participants\' experiences, which are stated in the policies.')
st.markdown('We will assume that you are an employee of a software organisation called *SoftOr*, and you must access the working room. Then, we will show you two different contexts and ask you to select your privacy preferences related to the data the working room requires. For the survey, we consider the policy of a single data, namely, your body shape – i.e., since you are accessing a working environment, you will be represented by an avatar that is close to your real physical aspect.')


# st.page_link("./pages/page1.py", label="Start")
# Button for navigation
columns = st.columns((2, 1, 2))
buttonStart = columns[1].button('Start the survey')
if buttonStart:
    # Redirect to another page
    st.switch_page("./pages/page2.py")

# pg = st.navigation([st.Page("./pages/page1.py"), st.Page("./pages/page2.py")], position="hidden",)
# pg.run()
