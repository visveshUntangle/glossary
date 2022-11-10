
pip install streamlit

!pip3 install -U datapane

import pandas as pd
import datapane as dp

df = pd.read_excel('attribute.xlsx' , sheet_name = "Subscriber Level")
# Attribute Name , Data category , Definition , 
df.head()

df = df.drop(['SAMPLE VALUES', 'LATENCY' , 'DATA TYPE' , 'DATA OWNER', 'FREQUENCY OF REFRESH', 'REDSHIFT TABLE', 'CFU', 'SUBJECT AREA', 'BRAND','DERIVATION TYPE','PII CATEGORY','PII SUBCATEGORY'], axis=1)

df

x = df['DATA CATEGORY'].value_counts()

y = x.plot(kind='bar');
y.set_title("Distribution of Attributes ")




dp.App(dp.Plot(y)).save(path="bar-plot.html")

"""Data Pane"""

# app = dp.App(dp.DataTable(df))

# app.save(path="simple-app.html", open=True)

df['DATA CATEGORY'].unique()

res_df = df[df['DATA CATEGORY'].isin(['Globe ID'])]
res_df

# app = dp.App(dp.DataTable(res_df))

"""Streamlit"""

import streamlit as st

st.title('Uber pickups in NYC')
