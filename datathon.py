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
