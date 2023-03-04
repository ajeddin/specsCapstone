import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
import numpy as np

import plotly.graph_objs as go

def load_data():
    
    happiness = pd.read_csv(r'dataframes/cleanhappiness.csv',index_col=[0])
    dfSuicide= pd.read_csv(r'cleanData.csv')
    ddTerr=pd.read_csv(r'dataframes/DST.csv')
    return happiness,dfSuicide,ddTerr
happiness,dfSuicide,ddTerr= load_data() #importing Dataframes
# # # # # # # # # # # # # # # DATA CLEANING # # # # # # # # # # # # # # # # # # # # #
dftest =dfSuicide.loc[dfSuicide['sex']==1].groupby('year',as_index=False).sum()
dftestWomen =dfSuicide.loc[dfSuicide['sex']==2].groupby('year',as_index=False).sum()
summed = dfSuicide.groupby('year',as_index=False).mean()
summedHapp = happiness.groupby('year',as_index=False).sum()
usaOnly = dfSuicide[dfSuicide['country']=='United States']
test =usaOnly.loc[usaOnly['sex']==1].groupby('year',as_index=False).sum()
testWomen =usaOnly.loc[usaOnly['sex']==2].groupby('year',as_index=False).sum()
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
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

embeded_linkedin={'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                    <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="HORIZONTAL" data-vanity="ajedev" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/ajedev?trk=profile-badge">Abdulaziz Jamaleddin</a></div>
              
              """}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def plot_male_happiness():
    fig, ax = plt.subplots()
    sns.lineplot(x='year',y='happy',ci=None,data=happiness[(happiness['female']==0)&(happiness['unem10']==0)&(happiness['divorce']==1)], ax=ax, color='blue',label="Employed/Divorced")
    sns.lineplot(x='year',y='happy',ci=None,data=happiness[(happiness['female']==0)&(happiness['divorce']==0)&(happiness['unem10']==0)], ax=ax, color='green',label="Employed/Not-Divorced")
    sns.lineplot(x='year',y='happy',ci=None,data=happiness[(happiness['female']==0)&(happiness['unem10']==1)&(happiness['divorce']==0)], ax=ax, color='purple',label="Unemployed/Not-Divorced")
    sns.lineplot(x='year',y='happy',ci=None,data=happiness[(happiness['female']==0)&(happiness['divorce']==1)&(happiness['unem10']==1)], ax=ax, color='red',label="Unemployed/Divorced")
    
    ax.set_title('Male Happiness Scale')
    ax.set_xlabel('Year')
    ax.set_ylabel('Happy Amount')
    ax.grid()
    ax.set_xlim(xmin=1994)
    ax.legend()
    
    st.pyplot(fig)

def plot_happiness_suicides_gender():
    fig, ax1 = plt.subplots(figsize=(6,3))

    sns.lineplot(x='year',y='happy',ci=None,data=happiness[(happiness['female']==0)], ax=ax1, color='blue',label="Male Happiness")
    sns.lineplot(x='year',y='happy',ci=None,data=happiness[(happiness['female']==1)], ax=ax1, color='red',label="Female Happiness")

    ax2 = ax1.twinx()
    sns.lineplot(x="year", y="percapita", data=test, ax=ax2, color='green', label='Male Suicides')
    sns.lineplot(x="year", y="percapita", data=testWomen,ax=ax2,color='pink',label='Female Suicides')
    ax1.set_xlim(xmin=1994)
    ax1.set_xlim(xmax=2006)
    ax1.grid()
    ax1.set_ylim(ymin=2)
    ax2.set_ylim(ymin=0)
    ax1.set_ylim(ymax=2.8)

    ax1.set_xlabel('Year')
    ax1.set_ylabel('Happiness')
    ax2.set_ylabel('Suicides')
    ax1.set_title('Happiness vs. Suicides in USA')
    ax1.legend(loc='upper left')

    st.pyplot(fig)

def plot_female_happiness():
    fig, ax = plt.subplots()
    sns.lineplot(x='year',y='happy',ci=None,data=happiness[(happiness['female']==1)&(happiness['unem10']==0)&(happiness['divorce']==1)], ax=ax, color='blue',label="Employed/Divorced")
    sns.lineplot(x='year',y='happy',ci=None,data=happiness[(happiness['female']==1)&(happiness['divorce']==0)&(happiness['unem10']==0)], ax=ax, color='green',label="Employed/Not-Divorced")
    sns.lineplot(x='year',y='happy',ci=None,data=happiness[(happiness['female']==1)&(happiness['unem10']==1)&(happiness['divorce']==0)], ax=ax, color='purple',label="Unemployed/Not-Divorced")
    sns.lineplot(x='year',y='happy',ci=None,data=happiness[(happiness['female']==1)&(happiness['divorce']==1)&(happiness['unem10']==1)], ax=ax, color='red',label="Unemployed/Divorced")

    ax.set_title('Female Happiness Scale')
    ax.set_xlabel('Year')
    ax.set_ylabel('Happy Amount')
    ax.grid()
    ax.set_xlim(xmin=1994)
    ax.legend()



###################################################################
#UNITED STATES PAGE
scatterGender = px.scatter(testTwo, x="gdp_per_capita", y="suicides/100kpop", color="sex", color_discrete_sequence=["blue", "red"])


suicides_gender_USA = px.line(test, x='year',y='percapita')
suicides_gender_USA.data[0].name="Male"
suicides_gender_USA['data'][0]['line']['color']='rgb(23, 54, 255)'
suicides_gender_USA.update_traces(showlegend=True)

suicides_gender_USA.add_scatter( x=testWomen['year'],y=testWomen['percapita'],name='Women')
suicides_gender_USA['data'][1]['line']['color']='rgb(237, 9, 9)'



# plot_happiness_suicides_gender = px.line(test, x='year',y='percapita')
# plot_happiness_suicides_gender.data[0].name="Male"
# plot_happiness_suicides_gender['data'][0]['line']['color']='rgb(23, 54, 255)'
# plot_happiness_suicides_gender.update_traces(showlegend=True)

# plot_happiness_suicides_gender.add_scatter( x=testWomen['year'],y=testWomen['percapita'],name='Women')
# plot_happiness_suicides_gender['data'][1]['line']['color']='rgb(237, 9, 9)'
# fig = go.Figure()

# fig.add_trace(go.Scatter(x=happiness[happiness['female'] == 0]['year'],
#                          y=happiness[happiness['female'] == 0].groupby('year',as_index=False).sum()['happy'],
#                          mode='lines',
#                          line=dict(color='blue'),
#                          name='Male Happiness', yaxis="y"))

# # Add female happiness line trace
# fig.add_trace(go.Scatter(x=happiness[happiness['female'] == 1]['year'],
#                          y=happiness[happiness['female'] == 1].groupby('year',as_index=False).sum()['happy'],
#                          mode='lines',
#                          line=dict(color='red'),
#                          name='Female Happiness', yaxis="y"))

# # Add male suicides line trace
# fig.add_trace(go.Scatter(x=test['year'],
#                          y=test['suicides_no'],
#                          mode='lines',
#                          line=dict(color='green'),
#                          name='Male Suicides',yaxis='y1'))

# # Add female suicides line trace
# fig.add_trace(go.Scatter(x=testWomen['year'],
#                          y=testWomen['percapita'],
#                          mode='lines',
#                          line=dict(color='pink'),
#                          name='Female Suicides',yaxis='y1'))

 
# # Create axis objects
# fig.update_layout(xaxis=dict(domain=[0.3, 0.7]),
 
#                   # create 1st y axis
#                   yaxis=dict(
#     title="yaxis title",
#     titlefont=dict(color="#1f77b4"),
#     tickfont=dict(color="#1f77b4")),
 
#     # create 2nd y axis
#     yaxis2=dict(title="yaxis2 title", overlaying="y",
#                 side="right", position=0.15) )

fig = go.Figure()

fig.add_trace(go.Scatter(x=happiness[happiness['female'] == 0]['year'],
                         y=happiness[happiness['female'] == 0]['happy'],
                         mode='lines',
                         line=dict(color='blue'),
                         name='Male Happiness'))

fig.add_trace(go.Scatter(x=summedHapp[summedHapp['female'] == 1]['year'],
                         y=summedHapp[summedHapp['female'] == 1]['happy'],
                         mode='lines',
                         line=dict(color='red'),
                         name='Female Happiness'))

fig.add_trace(go.Scatter(x=test['year'],
                         y=test['percapita'],
                         mode='lines',
                         line=dict(color='green'),
                         name='Male Suicides',
                         yaxis='y2'))

fig.add_trace(go.Scatter(x=testWomen['year'],
                         y=testWomen['percapita'],
                         mode='lines',
                         line=dict(color='pink'),
                         name='Female Suicides',
                         yaxis='y2'))

fig.update_layout(title='Happiness vs. Suicides in USA',
                  xaxis_title='Year',
                  yaxis=dict(title='Happiness', range=[0, 2000]),
                  yaxis2=dict(title='Suicides', overlaying='y', side='right', range=[0, .0003]),
                  legend=dict(x=0, y=1, traceorder='normal'))

###################################################################
#WORLDWIDE PAGE
barPlotGeneration =  px.bar(testTwo, x="generation", y="suicides_no", color="sex", barmode="group",
             color_discrete_sequence=['blue', 'red'])
barPlotGenerationUSA =  px.bar(testTwo[testTwo['country']=='United States'], x="generation", y="suicides_no", color="sex", barmode="group",
             color_discrete_sequence=['blue', 'red'])
lineplotSuicides = px.line(summed, x='year',y='suicides/100kpop')

worldwideSuicideGender = px.line(dftest, x='year',y='suicides_no')
worldwideSuicideGender.data[0].name="Male"
worldwideSuicideGender['data'][0]['line']['color']='rgb(23, 54, 255)'
worldwideSuicideGender.update_traces(showlegend=True)

worldwideSuicideGender.add_scatter( x=dftestWomen['year'],y=dftestWomen['suicides_no'],name='Women')
worldwideSuicideGender['data'][1]['line']['color']='rgb(237, 9, 9)'
###################################################################
#EXTRA 
# fig = go.Figure()

# fig.add_trace(go.Scatter(x=summedHapp[(summedHapp['female']==1)&(summedHapp['unem10']==1)&(summedHapp['divorce']==0)]['year'],
#                          y=summedHapp[(summedHapp['female']==1)&(summedHapp['unem10']==0)&(summedHapp['divorce']==1)]['happy'],
#                          mode='lines',
#                          line=dict(color='blue'),
#                          name='Employed/Divorced'))
# fig.add_trace(go.Scatter(x=summedHapp[(summedHapp['female']==1)&(summedHapp['unem10']==1)&(summedHapp['divorce']==0)]['year'],
#                          y=summedHapp[(summedHapp['female']==1)&(summedHapp['unem10']==0)&(summedHapp['divorce']==0)]['happy'],
#                          mode='lines',
#                          line=dict(color='green'),
#                          name='Employed/Not-Divorced'))
# fig.add_trace(go.Scatter(x=summedHapp[(summedHapp['female']==1)&(summedHapp['unem10']==1)&(summedHapp['divorce']==0)]['year'],
#                          y=summedHapp[(summedHapp['female']==1)&(summedHapp['unem10']==1)&(summedHapp['divorce']==0)]['happy'],
#                          mode='lines',
#                          line=dict(color='purple'),
#                          name='Unemployed/Not-Divorced'))
# fig.add_trace(go.Scatter(x=summedHapp[(summedHapp['female']==1)&(summedHapp['unem10']==1)&(summedHapp['divorce']==0)]['year'],
#                          y=summedHapp[(summedHapp['female']==1)&(summedHapp['unem10']==1)&(summedHapp['divorce']==1)]['happy'],
#                          mode='lines',
#                          line=dict(color='red'),
#                          name='Unemployed/Divorced'))



ddterr = px.line(ddTerr,y='ddfat',x='year')
ddterr.data[0].name="Drunk Driving Fatalities"
ddterr['data'][0]['line']['color']='rgb(23, 54, 255)'
ddterr.update_traces(showlegend=True)

ddterr.add_scatter( x=ddTerr['year'],y=ddTerr['nkill'],name='Deaths Caused by Terrorist Attacks')
ddterr['data'][1]['line']['color']='rgb(237, 9, 9)'
ddterr.add_scatter( x=ddTerr['year'],y=ddTerr['suicides'],name='Suicides Deaths')
ddterr['data'][2]['line']['color']='rgb(6, 299, 9)'
ddterr.update_xaxes(range=[1985, 2017])
###################################################################