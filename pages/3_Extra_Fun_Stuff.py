import streamlit as st
import streamlit.components.v1 as components
from functions import plot_male_happiness,plot_female_happiness,summed,fig,summedHapp
st. set_page_config(layout="wide",
    page_title='Extra Fun Analyzations',
    page_icon='🎉'
)
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Extra Fun Analyzations')
summedHapp

plot_male_happiness()
plot_female_happiness()
st.pyplot(plot_female_happiness())
st.plotly_chart(fig)

# st.line_chart(summed)


with st.sidebar:
    st.markdown("Developed by `Abdulaziz Jamaleddin`  ⇨  [GitHub Repo](https://github.com/ajeddin/specsCapstone).")
    st.markdown('___')