import pandas as pd
import numpy as np
import streamlit as st
from extract_cell_name import extract_cel_nam

df = pd.read_csv('2g-kpis.csv')
df=extract_cel_nam(df)
df.iloc[:,4:] = df.iloc[:,4:].replace('NIL', 0)
df.to_csv('clned.csv')

cells_tuple=df['Cell'].unique()
cells_tuple.sort()
cells_tuple=tuple(cells_tuple)
st.title("2G KPIs Dashboard")

option = st.selectbox(
    'Choose Cell',
    cells_tuple)


dfx=df[df['Cell']==str(option)]
st.title(str(option))
st.line_chart(data=dfx, x='Start Time', y='SD_AVAIL (%)', use_container_width=True)
st.line_chart(data=dfx, x='Start Time', y='cTCH Traffic (Erl)', use_container_width=True)
st.line_chart(data=dfx, x='Start Time', y='S3655:Number of configured TRXs in a cell (None)', use_container_width=True)
st.line_chart(data=dfx, x='Start Time', y='BSS CSSR (%)', use_container_width=True)
st.line_chart(data=dfx, x='Start Time', y='Radio_Handover Success Rate (%)', use_container_width=True)




