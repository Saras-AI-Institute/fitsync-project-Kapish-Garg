import numpy as np
import pandas as pd
from datetime import timedelta, date
import random

# Function to generate date range
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days) + 1):
        yield date1 + timedelta(n)

# Generate dates for the year 2025
dates = list(daterange(date(2025, 1, 1), date(2025, 12, 31)))

# Generate synthetic data
data = {
    'Date': dates,
    'Steps': np.random.normal(loc=8500, scale=2500, size=365).clip(3000, 18000),
    'Sleep_Hours': np.random.normal(loc=7.2, scale=1, size=365).clip(4.5, 9.5),
    'Heart_Rate_bpm': np.random.normal(loc=68, scale=10, size=365).clip(48, 110),
    'Calories_Burned': np.random.uniform(1800, 4200, 365),
    'Active_Minutes': np.random.uniform(20, 180, 365)
}

# Create DataFrame
df = pd.DataFrame(data)

# Introduce 5% NaN values randomly in each column
num_nan = int(0.05 * len(df))
for column in df.columns[1:]:  # Skip the Date column
    nan_indices = random.sample(range(len(df)), num_nan)
    df.loc[nan_indices, column] = np.nan

# Save to CSV file
df.to_csv('data/health_data.csv', index=False)