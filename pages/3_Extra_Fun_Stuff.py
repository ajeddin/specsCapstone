import streamlit as st
import streamlit.components.v1 as components
from functions import plot_male_happiness,plot_female_happiness
st. set_page_config(layout="wide",
    page_title='Extra Fun Analyzations',
    page_icon='🎉'
)

st.title('Extra Fun Analyzations')


plot_male_happiness()
plot_female_happiness()





with st.sidebar:
    st.markdown("Developed by `Abdulaziz Jamaleddin`  ⇨  [GitHub Repo](https://github.com/ajeddin/specsCapstone).")
    st.markdown('___')