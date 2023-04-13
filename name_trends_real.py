import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'
df = pd.read_csv(url)

pattern = st.text_input("Type a name to search", placeholder="Enter a name or regular expression")

st.write('Generating plot for', pattern)

st.title('Name Plot')

st.set_option('deprecation.showPyplotGlobalUse', False)
selected_name = pattern
name_df = df[df['name']==selected_name]
sns.lineplot(data=name_df, x='year', y='n', hue='sex')
plt.title(f'Name Trend for {selected_name} from 1910-2021')
plt.legend(loc=(1.01,0))
st.pyplot()
