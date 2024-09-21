import streamlit as st
import plotly.express as px

# Add title
st.title("Diary Tone")

# Plot positivity 
st.subheader("Positivity")
x = ['2024-09-20', '2024-09-21', '2024-09-22']
y = [0.9, 0.2, 0.6]
figure = px.line(x=x, y=y, 
                 labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)


# Plot negativity
st.subheader("Negativity")
x = ['2024-09-20', '2024-09-21', '2024-09-22']
y = [0.2, 0.6, 0.3]
figure = px.line(x=x, y=y, 
                 labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure)