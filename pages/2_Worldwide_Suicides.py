import streamlit as st
import streamlit.components.v1 as components
from functions import lineplotSuicides,barPlotGeneration,worldwideSuicideGender
st. set_page_config(layout="wide",
    page_title='Worldwide Suicides Analysis',
    page_icon='🌍'
)
st.title('Worldwide Suicides Analysis') 
st.header('Women commit less suicide compared to men worldwide')
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


col1,col2 = st.columns((1,1))
with col1:
    st.plotly_chart(barPlotGeneration,use_container_width=True)
    
with col2:
    st.plotly_chart(worldwideSuicideGender,use_container_width=True)
st.plotly_chart(lineplotSuicides,use_container_width=True)




with st.sidebar:
    st.markdown("Developed by `Abdulaziz Jamaleddin`  ⇨  [GitHub Repo](https://github.com/ajeddin/specsCapstone).")
    st.markdown('___')


hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)