import streamlit as st
from modules.processor import process_data
import pandas as pd
import plotly.express as px

# Set the Streamlit page configuration
st.set_page_config(layout="wide", page_title="Trends & Insights")

# Title for the page
st.title("Trends & Insights")

# Load and process the data
processed_data = process_data()

# Add a sidebar for time filtering
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days", "Last 30 Days", "All Time"],
    index=2
)

def filter_data_by_time(data, time_range):
    if 'Date' in data.columns:
        max_date = data['Date'].max()
        if time_range == "Last 7 Days":
            min_date = max_date - pd.Timedelta(days=7)
            return data[data['Date'] >= min_date]
        elif time_range == "Last 30 Days":
            min_date = max_date - pd.Timedelta(days=30)
            return data[data['Date'] >= min_date]
    return data  # For "All Time"

# Filter the data based on the sidebar selection
filtered_data = filter_data_by_time(processed_data, time_range)

# Calculate and display summary statistics
st.write("### Summary Statistics")
for column in ['Recovery_Score', 'Sleep_Hours', 'Steps', 'Calories_Burned']:
    st.write(f"*{column.replace('_', ' ')}:*")
    st.write(f"Mean: {filtered_data[column].mean():.2f}")
    st.write(f"Min: {filtered_data[column].min():.2f}")
    st.write(f"Max: {filtered_data[column].max():.2f}")
    st.write("---")

# Line chart for average Recovery Score month-wise
st.write("### Monthly Average Recovery Score")
# Update month column for JSON serialization compatibility
filtered_data['Month'] = filtered_data['Date'].dt.to_period('M').astype(str)
monthly_avg_recovery = filtered_data.groupby('Month')['Recovery_Score'].mean().reset_index()
line_fig = px.line(monthly_avg_recovery, x='Month', y='Recovery_Score', title='Monthly Average Recovery Score')
st.plotly_chart(line_fig)

# Histograms for distribution
st.write("### Distributions of Key Metrics")
metrics = {'Steps': "Steps", 'Calories_Burned': "Calories Burned", 'Recovery_Score': "Recovery Score", 'Sleep_Hours': "Sleep Hours"}
for metric, label in metrics.items():
    hist_fig = px.histogram(filtered_data, x=metric, title=f'Distribution of {label}')
    st.plotly_chart(hist_fig)

# Explanation:
# - Reuse time filter logic to allow data filtering based on user selection.
# - Summary statistics are provided for selected metrics.
# - Visualization of monthly average trends and distributions using Plotly.