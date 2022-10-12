import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
import plotly.express as px


st.set_page_config(page_title = 'TASK')
st.header('TASK - 5')
st.subheader('Temperature of the Cities')

data = pd.read_csv('Temperature_Cities.csv')
#st.dataframe(data.head())

submit = st.checkbox('First')
if submit:
   st.dataframe(data)
st.radio('Which one of the City Highest Avg Rate : ',('Chennai','Bombay','Calcutta'))

columns = list(data.columns)
#Target = st.selectbox('choose a target:',columns)
col2 = columns.copy()
#col2.remove(Target)
x_var = st.selectbox('Choose a City1: ', col2)
y_var = st.selectbox('Choose b City2: ', col2)

#source = pd.DataFrame({"category": [1, 2, 3, 4, 5, 6], "value": [4, 6, 10, 3, 7, 8]})

#fig_category_percent=alt.Chart(source).mark_arc().encode(
#    theta=alt.Theta(field="value", type="quantitative"),
#    color=alt.Color(field="category", type="nominal"))
#st.altair_chart(fig_category_percent)


"Chennai"
source = pd.DataFrame({
        'Temperature of the City': [35, 36, 39, 40],
        'Days': ['Day1', 'Day2', 'Day3', 'Day4']
     })
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Temperature of the City:Q',
        x='Days:O',
    )
 
st.altair_chart(bar_chart, use_container_width=True)


"Bombay"
source = pd.DataFrame({
        'Temperature of the City': [45, 43, 41, 42],
        'Days': ['Day1', 'Day2', 'Day3', 'Day4']
     })
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Temperature of the City:Q',
        x='Days:O',
    )
 
st.altair_chart(bar_chart, use_container_width=True)



"Calcutta"
source = pd.DataFrame({
        'Temperature of the City': [35, 34, 36, 39],
        'Days': ['Day1', 'Day2', 'Day3', 'Day4']
     })
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Temperature of the City:Q',
        x='Days:O',
    )
 
st.altair_chart(bar_chart, use_container_width=True)






