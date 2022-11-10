
import streamlit as st
import pandas as pd
# import openpyxl

df = pd.read_csv('attribute.csv')

df = df.drop(['SAMPLE VALUES', 'LATENCY' , 'DATA TYPE' , 'DATA OWNER', 'FREQUENCY OF REFRESH', 'REDSHIFT TABLE', 'CFU', 'SUBJECT AREA', 'BRAND','DERIVATION TYPE','PII CATEGORY','PII SUBCATEGORY'], axis=1)

# df


x = df['DATA CATEGORY'].value_counts()

# y = x.plot(kind='bar');
# y.set_title("Distribution of Attributes ")
st.write("Distribution of attributes")
st.bar_chart(x)



option = st.selectbox(
    'Select category of Attribute',
     df['DATA CATEGORY'].unique())

'You selected: ', option




res_df = df[df['DATA CATEGORY'].isin([option])]

st.metric(label= "Number of Attributes" ,value= res_df.shape[0])

res = res_df.drop(['DATA CATEGORY'],axis= 1)

st.table(res)