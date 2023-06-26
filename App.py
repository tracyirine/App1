import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
st.title("CMal Dashboard")
st.subheader('clinical malaria predictors')



df = pd.read_csv("Clinical.csv") 
st.title("Clinical malaria")
st.write(df)



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("Clinical.csv") 
df.info()
df.duplicated()
df.count()
df.dropna()


st.sidebar.header("Cmal Dash:")
RDT=st.sidebar.multiselect( 
"Select the RDT:",
 options=df["RDT"].unique(),
 default=df["RDT"].unique()
)

Microscopy=st.sidebar.multiselect( 
"Select the Microscopy:",
 options=df["Microscopy"].unique(),
 default=df["Microscopy"].unique()
)

Clinical_Diagnosis=st.sidebar.multiselect( 
"Select the Clinical_Diagnosis:",
 options=df["Clinical_Diagnosis"].unique(),
 default=df["Clinical_Diagnosis"].unique()
)

fever_symptom=st.sidebar.multiselect( 
"Select the fever_symptom:",
 options=df["fever_symptom"].unique(),
 default=df["fever_symptom"].unique()
)

df = pd.read_csv("Clinical.csv")

df.dropna()

st.write("""
Average hb_level, Grouped by Microscopy
""")
hb_level = df.groupby('Microscopy')['hb_level'].mean().round()
hb_level = hb_level.reset_index()
Microscopy = hb_level['Microscopy']
avg_hb= hb_level['hb_level']

fig = plt.figure(figsize = (19, 10))

plt.bar(Microscopy, avg_hb, color = 'maroon')
plt.xlabel('Microscopy')
plt.ylabel('hb_level')
plt.title('Matplotlib Bar Chart showing average Hb_level in Microscopy outcome')
st.pyplot(fig)




st.write("""
Average wbc_count, Grouped by Microscopy
""")
wbc_count = df.groupby('Microscopy')['wbc_count'].mean().round()
wbc_count = wbc_count.reset_index()
Microscopy = wbc_count['Microscopy']
avg_wbc= wbc_count['wbc_count']

fig = plt.figure(figsize = (19, 10))

plt.bar(Microscopy, avg_wbc, color = 'blue')
plt.xlabel('Microscopy')
plt.ylabel('wbc_count')
plt.title('Matplotlib Bar Chart showing average wbc_count in Microscopy outcome')
st.pyplot(fig)

st.subheader('Microscopy Results')
plt.figure(figsize=(10, 6))
df['Microscopy'].value_counts().plot(kind='bar')
plt.xlabel('Microscopy')
plt.ylabel('Count')
plt.title('Microscopy Results')
st.pyplot(fig)

st.subheader('Rapid Diagnostic Test (RDT) Results')
plt.figure(figsize=(10, 6))
df['RDT'].value_counts().plot(kind='bar')
plt.xlabel('Rapid Diagnostic Test (RDT)')
plt.ylabel('Count')
plt.title('RDT')
st.pyplot(fig)















