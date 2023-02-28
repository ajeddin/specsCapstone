import streamlit as st
import streamlit.components.v1 as components
from functions import lineplotSuicides,barPlotGeneration,worldwideSuicideGender
st. set_page_config(layout="wide",
    page_title='Worldwide Suicides Analysis',
    page_icon='🌍'
)
st.title('Worldwide Suicides Analysis') 
################################################################
lineplotSuicides.update_layout(
    title="Worldwide Suicides per 100k",
    xaxis_title="Year",
    yaxis_title="Suicides per 100k population"
)
barPlotGeneration.update_layout(
    title="Worldwide Suicides Grouped by Generation",
    xaxis_title="Generation",
    yaxis_title="Suicides"
)
worldwideSuicideGender.update_layout(
    title="Worldwide Suicides Based on Gender",
    xaxis_title="Year",
    yaxis_title="Suicides"
)
################################################################

st.plotly_chart(lineplotSuicides)
st.plotly_chart(barPlotGeneration)
st.plotly_chart(worldwideSuicideGender)





with st.sidebar:
    st.markdown("Developed by `Abdulaziz Jamaleddin`  ⇨  [GitHub Repo](https://github.com/ajeddin/specsCapstone).")
    st.markdown('___')


hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)