import streamlit as st
import pandas as pd
import plotly.express as px

st.title("NBA Player Performance Tracker")
df = pd.read_csv('csv\\player_season_stats.csv')  # Your cleaned data
player = st.selectbox("Select Player", df['personName'].unique())
player_data = df[df['personName'] == player]
fig = px.line(player_data, x='season_year', y='points', title=f"{player} PPG Trend")
st.plotly_chart(fig)