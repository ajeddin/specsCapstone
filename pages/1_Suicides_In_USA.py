import streamlit as st
import streamlit.components.v1 as component
from functions import suicides_gender_USA,plot_happiness_suicides_gender,testTwo,scatterGender,barPlotGenerationUSA
st. set_page_config(layout="wide",
    page_title='Suicides in USA Analysis',
    page_icon='☠️'
)
###############################################################
scatterGender.update_layout(
    title="Suicides and GDP per Capita",
    xaxis_title="GDP per Capita",
    yaxis_title="Suicides per 100k population"
)
barPlotGenerationUSA.update_layout(
    title="Worldwide Suicides Grouped by Generation USA",
    xaxis_title="Generation",
    yaxis_title="Suicides"
)
suicides_gender_USA.update_layout(
    title="Suicides in USA based on gender (per capita)",
    xaxis_title="Year",
    yaxis_title="Suicides (per capita)"
)

###############################################################
st.title('Suicides in USA Analysis')
st.header('Women commit less suicide compared to men in the US')

col1,col2 = st.columns((1,1))
with col1:
    st.plotly_chart(scatterGender,use_container_width=True )
with col2:
    st.plotly_chart(barPlotGenerationUSA,use_container_width=True)

# st.plotly_chart(scatterGender)
# st.plotly_chart(barPlotGenerationUSA)
st.plotly_chart(suicides_gender_USA,use_container_width=True)
plot_happiness_suicides_gender()


with st.sidebar:
    st.markdown("Developed by `Abdulaziz Jamaleddin`  ⇨  [GitHub Repo](https://github.com/ajeddin/specsCapstone).")
    st.markdown('___')


hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)