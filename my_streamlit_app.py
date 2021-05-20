import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

df_cars['continent'] = df_cars['continent'].apply(lambda x: x.strip().replace('.',''))

selected_continent = st.sidebar.selectbox(
    label="Select continent to filter", options = df_cars['continent'].unique()
)

df = df_cars[df_cars['continent'] == selected_continent]

st.title('Hello Wilders, welcome to my application!')

#Dataframe
st.write(f'DataFrame of {selected_continent} below :')
df_cars[df_cars['continent'] == selected_continent]

#Heartmap
fig1, ax1 = plt.subplots()
mask = np.triu(np.ones_like(df.corr(), dtype = np.bool))
ax1 = sns.heatmap(data = df.corr(),
                  mask = mask,
                  annot = True,
                  cmap = sns.color_palette("vlag",
                  as_cmap = True))   
ax1.set_title(f'Heartmap of {selected_continent}')

st.pyplot(fig1)

#Dont work : #lmplot #displot #relplot #catplot #jointplot

#scatterplot
fig2, ax2 = plt.subplots()
ax2 = sns.scatterplot(data = df,
                      x = "hp",
                      y = "weightlbs",
                      hue = "cylinders")

st.pyplot(fig2)

#lineplot
fig3, ax3 = plt.subplots()

ax3 = sns.lineplot(data = df,
                      x = "hp",
                      y = "weightlbs",
                      hue = "cylinders")

st.pyplot(fig3)

#boxplot
fig4, ax4 = plt.subplots()

ax4 = sns.boxplot(data = df,
                      x = "continent",
                      y = "weightlbs",
                      hue = "cylinders")
st.pyplot(fig4)

#violinplot
fig5, ax5 = plt.subplots()

ax5 = sns.violinplot(data = df,
                      x = "continent",
                      y = "weightlbs",
                      hue = "cylinders")
st.pyplot(fig5)

#histplot
fig6, ax6 = plt.subplots()

ax6 = sns.histplot(data = df,
                      x = "hp",
                      y = "weightlbs",
                      hue = "cylinders")
st.pyplot(fig6)

#https://seaborn.pydata.org/examples/index.html
