import streamlit as st
import streamlit.components.v1 as components
from functions import plot_male_happiness,plot_female_happiness,ddterr
st. set_page_config(layout="wide",
    page_title='Extra Fun Analyzations',
    page_icon='🎉'
)
st.set_option('deprecation.showPyplotGlobalUse', False)
################################################################
ddterr.update_layout(
    title="Deaths in USA",
    xaxis_title="Year",
    yaxis_title="Number of Deaths"
)
################################################################
st.title('Extra Fun Analyzations')


st.plotly_chart(ddterr,use_container_width=True)
col1,col2 = st.columns((1,1))
with col1:
    plot_male_happiness()
with col2:
    st.pyplot(plot_female_happiness())
# st.line_chart(summed)

with st.sidebar:
    st.markdown("Developed by `Abdulaziz Jamaleddin`  ⇨  [GitHub Repo](https://github.com/ajeddin/specsCapstone).")
    st.markdown('___')