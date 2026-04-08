import streamlit as st
from modules.processor import process_data
import pandas as pd

# Set the page configuration
st.set_page_config(layout="wide", page_title="FitSync")

# Main title of the Streamlit app
st.title("FitSync - Personal Health Analytics")

# Load the processed data
with st.spinner("Loading and processing data..."):
    df = process_data()

# Sidebar for filters
st.sidebar.header("Filters")

# Dynamic time range selection
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days", "Last 30 Days", "All Time"],
    index=2
)

# Adjust dataframe based on time range selection
# today = pd.Timestamp("today")
today = df['Date'].max()
if time_range == "Last 7 Days":
    start_date = today - pd.Timedelta(days=7)
    df_filtered = df[df['Date'] >= start_date]
elif time_range == "Last 30 Days":
    start_date = today - pd.Timedelta(days=30)
    df_filtered = df[df['Date'] >= start_date]
else:
    df_filtered = df  # Use full dataframe for "All Time"

# Recalculate metrics based on the filtered dataframe
average_steps = df_filtered['Steps'].mean()
average_sleep_hours = df_filtered['Sleep_Hours'].mean()
average_recovery_score = df_filtered['Recovery_Score'].mean()

# Display metrics in three columns
col1, col2, col3 = st.columns(3)
col1.metric(label="Average Steps", value=f"{average_steps:.0f}")
col2.metric(label="Average Sleep Hours", value=f"{average_sleep_hours:.1f}")
col3.metric(label="Average Recovery Score", value=f"{average_recovery_score:.1f}")

# Display the processed health data
st.subheader("Processed Health Data")
# Display dataframe in a table format
st.dataframe(df_filtered)

# Display some summary statistics
st.subheader("Summary Statistics")
# Generate and display summary statistics
st.write(df_filtered.describe())

# Allow users to download the processed data
st.subheader("Download Processed Data")
st.download_button(
    label="Download as CSV",
    data=df_filtered.to_csv(index=False),
    file_name=f"processed_health_data_{time_range.replace(' ', '_').lower()}.csv",
    mime="text/csv"
)

st.success("Data successfully loaded and processed!")

