import streamlit as st
import streamlit.components.v1 as components
from functions import embeded_linkedin
st. set_page_config(layout="wide",
    page_title='Purpose',
    page_icon='👋'
)

st.title('About Me:')

col1,col2,col3 = st.columns((1,1,1))
with col1:
    st.markdown('#### Hey, My name is `Abdulaziz Jamaleddin`!')
    st.markdown('#### I am a Software Dev and a Data Analyst.')
with col3:
    components.html(embeded_linkedin['linkedin'],height=300)


st.write('# Purpose')
st.markdown('### The goal of this study is to illustrate suicide rates between men and females')
st.markdown('##### 👈 Select a Page')

col1,col2 = st.columns((1,1))

with col1:
    st.write('# Sources:')
    st.write('### - [Suicide Rates Overview 1985 to 2016](https://www.kaggle.com/datasets/russellyates88/suicide-rates-overview-1985-to-2016)')
    st.write('### - [Happiness in USA](https://vincentarelbundock.github.io/Rdatasets/csv/wooldridge/happiness.csv)')
    st.write('### - [Casualties/Fatalities in the U.S. for Drunk-Driving, Suicide, and Terrorism](https://vincentarelbundock.github.io/Rdatasets/csv/stevedata/DST.csv/)')

with col2:
    st.write('# Tech Used:')
    st.write('### - [Python](https://www.python.org/) | [Jupyter Notebook](https://jupyter.org/) | [Anaconda](https://www.anaconda.com/)')
    st.write('### - [Pandas](https://pandas.pydata.org/) | [Numpy](https://numpy.org/) | [Statsmodels](https://www.statsmodels.org/stable/index.html) | [Sklearn](https://scikit-learn.org/stable/#)')
    st.write('### - [Matplotlib](https://matplotlib.org/) | [Seaborn](https://seaborn.pydata.org/) | [Plotly](https://plotly.com/python/)')


# st.sidebar.success('👆 Select a page above 👆')
with st.sidebar:
    # st.markdown('___')
    st.markdown("Developed by `Abdulaziz Jamaleddin`  ⇨  [GitHub Repo](https://github.com/ajeddin/specsCapstone).")
    st.markdown('___')

hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)