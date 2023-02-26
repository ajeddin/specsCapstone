import streamlit as st
import streamlit.components.v1 as components
from functions import embeded_linkedin
st. set_page_config(layout="wide",
    page_title='Worldwide Suicides Analysis',
    page_icon='🌍'
)

st.title('Worldwide Suicides Analysis')

with st.sidebar:
    st.markdown("Developed by `Abdulaziz Jamaleddin`  ⇨  [GitHub Repo](https://github.com/ajeddin/specsCapstone).")
    st.markdown('___')