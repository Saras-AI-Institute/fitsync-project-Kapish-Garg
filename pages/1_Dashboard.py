import streamlit as st
from modules.processor import process_data
import pandas as pd
import plotly.express as px

# Set the Streamlit page configuration
st.set_page_config(layout="wide", page_title="FitSync")

# Title for the dashboard
st.title("FitSync - Personal Health Analytics")

# Load and process the data
# This will retrieve the final processed DataFrame
processed_data = process_data()

# Add a sidebar for time filtering
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days", "Last 30 Days", "All Time"],
    index=2
)

# Filter data based on the selected time range
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

# Calculate and display metrics from the filtered data
st.write("### Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric(label="Average Steps", value=f"{filtered_data['Steps'].mean():.0f}")
col2.metric(label="Average Sleep Hours", value=f"{filtered_data['Sleep_Hours'].mean():.1f}")
col3.metric(label="Average Recovery Score", value=f"{filtered_data['Recovery_Score'].mean():.1f}")

# Visualization - Dual Line Chart
st.write("### Trends & Insights")
line_col1, line_col2 = st.columns(2)
with line_col1:
    st.write("#### Recovery Score & Sleep Trend")
    recovery_sleep_fig = px.line(
        filtered_data,
        x='Date',
        y=['Recovery_Score', 'Sleep_Hours'],
        title='Recovery Score & Sleep Trend',
        labels={'value': 'Value', 'variable': 'Metric'}
    )
    st.plotly_chart(recovery_sleep_fig)

with line_col2:
    st.write("#### Recovery Score vs Daily Steps")
    scatter_fig_steps = px.scatter(
        filtered_data,
        x='Steps',
        y='Recovery_Score',
        color='Sleep_Hours',
        title='Recovery Score vs Daily Steps',
        labels={'x': 'Daily Steps', 'y': 'Recovery Score', 'color': 'Sleep Hours'}
    )
    st.plotly_chart(scatter_fig_steps)

# Visualization - Additional Scatter and Line Charts
scatter_col1, scatter_col2 = st.columns(2)
with scatter_col1:
    st.write("#### Recovery Score vs Resting Heart Rate")
    scatter_fig_hr = px.scatter(
        filtered_data,
        x='Heart_Rate_bpm',
        y='Recovery_Score',
        title='Recovery Score vs Resting Heart Rate',
        labels={'x': 'Heart Rate (bpm)', 'y': 'Recovery Score'}
    )
    st.plotly_chart(scatter_fig_hr)

with scatter_col2:
    st.write("#### Daily Calories Burned Trend")
    calories_fig = px.line(
        filtered_data,
        x='Date',
        y='Calories_Burned',
        title='Daily Calories Burned Trend',
        labels={'x': 'Date', 'y': 'Calories Burned'}
    )
    st.plotly_chart(calories_fig)
# Display the data in a table format
st.write("### Processed Health Data")
st.dataframe(processed_data)

# Additional features or sections can be added below to enhance the dashboard
# For example, visualizations, user inputs, analytics summaries, etc.