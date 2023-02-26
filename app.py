import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statsmodels.api as sm
from scipy.stats import pearsonr
from scipy import stats
import plotly.graph_objs as go
import plotly.express as px



st.set_page_config(page_title="Suicide and Happiness Analysis", page_icon=":sunglasses:", layout="wide")
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

happiness = pd.read_csv('cleanHappiness.csv',index_col=[0])
dfSuicide = pd.read_csv('cleanData.csv')
ddTerr = pd.read_csv('DST.csv')
usaOnly = dfSuicide[dfSuicide['country']=='United States']
test =usaOnly.loc[usaOnly['sex']==1].groupby('year').sum()
testWomen =usaOnly.loc[usaOnly['sex']==2].groupby('year').sum()
testWomen['percapita'] = testWomen['suicides_no']/testWomen['population']
test['percapita'] = test['suicides_no']/test['population']
testTwo=dfSuicide.copy()
testTwo.sex[testTwo.sex == 1] = "Male"
testTwo.sex[testTwo.sex == 2] = "Female"
testTwo.generation[testTwo.generation == 1] = 'G.I.'
testTwo.generation[testTwo.generation == 2] = 'Silent'
testTwo.generation[testTwo.generation == 3] = 'Boomers'
testTwo.generation[testTwo.generation == 4] = 'X'
testTwo.generation[testTwo.generation == 5] = 'Millennials'
testTwo.generation[testTwo.generation == 6] = 'Z'

def plot_happiness():
    # Create the plot
    fig, ax = plt.subplots()
    sns.lineplot(x='year',y='happy',ci=None,data=happiness[(happiness['female']==0)&(happiness['unem10']==0)&(happiness['divorce']==1)], ax=ax, color='blue',label="Employed/Divorced")
    sns.lineplot(x='year',y='happy',ci=None,data=happiness[(happiness['female']==0)&(happiness['divorce']==0)&(happiness['unem10']==0)], ax=ax, color='green',label="Employed/Not-Divorced")
    sns.lineplot(x='year',y='happy',ci=None,data=happiness[(happiness['female']==0)&(happiness['unem10']==1)&(happiness['divorce']==0)], ax=ax, color='purple',label="Unemployed/Not-Divorced")
    sns.lineplot(x='year',y='happy',ci=None,data=happiness[(happiness['female']==0)&(happiness['divorce']==1)&(happiness['unem10']==1)], ax=ax, color='red',label="Unemployed/Divorced")
    
    # Set plot attributes
    ax.set_title('Male Happiness Scale')
    ax.set_xlabel('Year')
    ax.set_ylabel('Happy Amount')
    ax.grid()
    ax.set_xlim(xmin=1994)
    ax.legend()
    
    # Show the plot
    st.pyplot(fig)

# Create the Streamlit app
st.title('Male Happiness Scale Visualization')
plot_happiness()

fig = px.scatter(testTwo, x="gdp_per_capita", y="suicides/100kpop", color="sex", color_discrete_sequence=["blue", "red"])

# Add title and axis labels
fig.update_layout(
    title="Suicides and GDP per Capita",
    xaxis_title="GDP per Capita",
    yaxis_title="Suicides per 100k population"
)

# Render the plot using Streamlit
st.plotly_chart(fig)

fig = px.bar(testTwo, x="generation", y="suicides_no", color="sex",color_discrete_sequence=["blue", "red"])

# Set axis titles and plot title
fig.update_layout(
    xaxis_title="Generation",
    yaxis_title="Number of Suicides",
    title="Number of Suicides by Generation and Sex"
)

# Display plot using Streamlit
st.plotly_chart(fig)



fig = px.line(happiness[(happiness['female']==0)&(happiness['unem10']==0)&(happiness['divorce']==1)],x='year',y='happy')
