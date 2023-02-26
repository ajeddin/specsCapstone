import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import plotly.express as px
def load_data():
    happiness = pd.read_csv(r'dataframes/cleanhappiness.csv',index_col=[0])
    dfSuicide= pd.read_csv(r'dataframes/cleanData.csv')
    ddTerr=pd.read_csv(r'dataframes/DST.csv')
    return happiness,dfSuicide,ddTerr
happiness,dfSuicide,ddTerr= load_data() #importing Dataframes
# # # # # # # # # # # # # # # DATA CLEANING # # # # # # # # # # # # # # # # # # # # #
# Prices Dataframe Cleaning
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
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

embeded_linkedin={'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                    <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="ajedev" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/ajedev?trk=profile-badge"></a></div>"""}

