import pandas as pd
import requests
import plotly.express as px
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

link = 'https://raw.githubusercontent.com/marcthavy/MyStreamlitApp/main/data/'

csv_cc_01 = 'Satellites.csv'

df = pd.read_csv(link + csv_cc_01, sep = ';')

df['Launch']=df['Launch'].replace('TBD','')
df['Launch']=pd.to_datetime(df['Launch'])
df['(expected) EOL']=df['(expected) EOL'].replace('TBD','')
df['(expected) EOL']=pd.to_datetime(df['(expected) EOL'])

df['Life time']=pd.to_timedelta(df['(expected) EOL']-df['Launch'],unit='days')
df['Life time']=pd.to_numeric(df['Life time'].dt.days, downcast='integer')

#fig = px.area(df, x='Launch' , y='Life time', range_x=['1960','2021'])
#fig.show() 

fig = px.line(df, x='Launch' , y='(expected) EOL', range_x=['1960','2021'], title='Life Time of launched sattelites')

st.plotly_chart(fig)

df2=pd.read_excel('/work/Satellites/sattelites CEOS.xlsx')

def translate(x):
    dictionnaire = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12',
    'Sep': '09'}
    if type(x) == str:
        for i, j in dictionnaire.items():
            if i in x:
                x = x.replace(i, j)
                return x   
    else:
        return x

df2['Launch Date'] = df2['Launch Date'].apply(translate)
df2['Launch Date']=df2['Launch Date'].astype(str)
df2['Launch Date']=pd.to_datetime(df2['Launch Date'])

df2['EOL Date'] = df2['EOL Date'].apply(translate)
df2['EOL Date']=df2['EOL Date'].astype(str)
df2['EOL Date']=pd.to_datetime(df2['EOL Date'])

df2 = df2.sort_values(['Launch Date', 'EOL Date'], ascending = (False, True))

fig = px.line(df2, x='Launch Date' , y='EOL Date', title='Life Time of launched sattelites')

st.plotly_chart(fig)
