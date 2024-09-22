import streamlit as st
import plotly.express as px
from backend import get_data

# Add title
st.title("Diary Tone")

# Plot positivity 
st.subheader("Positivity")
dates, scores = get_data("pos")
figure = px.line(x=dates, y=scores, 
                 labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)


# Plot negativity
st.subheader("Negativity")
dates, scores = get_data("neg")
figure = px.line(x=dates, y=scores, 
                 labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure)