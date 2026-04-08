import pandas as pd


def load_data():
    # Path to the CSV file
    file_path = 'data/health_data.csv'

    # Load the CSV file into a DataFrame
    health_data = pd.read_csv(file_path)

    # Fill missing 'Steps' with the median value of the column
    health_data['Steps'].fillna(health_data['Steps'].median(), inplace=True)
    
    # Fill missing 'Sleep_Hours' with 7.0
    health_data['Sleep_Hours'].fillna(7.0, inplace=True)
    
    # Fill missing 'Heart_Rate_bpm' with 68
    health_data['Heart_Rate_bpm'].fillna(68, inplace=True)
    
    # Fill missing values in other columns with their respective medians
    for column in health_data.columns:
        if column not in ['Date', 'Steps', 'Sleep_Hours', 'Heart_Rate_bpm']:
            health_data[column].fillna(health_data[column].median(), inplace=True)
    
    # Convert the 'Date' column to datetime objects
    health_data['Date'] = pd.to_datetime(health_data['Date'])
    
    # Return the cleaned DataFrame
    return health_data  


def calculate_recovery_score(df):
    """
    This function calculates a 'Recovery_Score' based on Sleep_Hours, Heart_Rate_bpm, and Steps.
    The score is between 0 and 100, where higher scores indicate better recovery.
    """

    # Initialize recovery score with a base value of 50
    df['Recovery_Score'] = 50

    # Adjust score based on Sleep_Hours
    # - 7+ hours considered good, heavily boosts recovery score
    df.loc[df['Sleep_Hours'] >= 7, 'Recovery_Score'] += 20
    # - Less than 6 hours significantly reduces recovery score
    df.loc[df['Sleep_Hours'] < 6, 'Recovery_Score'] -= 20

    # Adjust score based on Heart_Rate_bpm
    # - Heart rates lower than 60 significantly increase the recovery score
    df.loc[df['Heart_Rate_bpm'] < 60, 'Recovery_Score'] += 15
    # - Heart rates above 80 slightly decrease the recovery score
    df.loc[df['Heart_Rate_bpm'] > 80, 'Recovery_Score'] -= 10

    # Adjust score based on Steps
    # - High activity levels (above 12000 steps) slightly reduce recovery score due to strain
    df.loc[df['Steps'] > 12000, 'Recovery_Score'] -= 5
    # - Moderate activity (6000-12000 steps) slightly improves recovery
    df.loc[(df['Steps'] >= 6000) & (df['Steps'] <= 12000), 'Recovery_Score'] += 5

    # Ensure Recovery_Score stays within 0 and 100
    df['Recovery_Score'] = df['Recovery_Score'].clip(0, 100)

    return df

# This module can be imported and `load_data()` can be called to obtain the cleaned DataFrame.
# Adding function to the module, which can be called to compute the recovery score

def process_data():
    # Call load_data() to get the cleaned DataFrame
    df = load_data()

    # Call calculate_recovery_score() to add the Recovery Score
    df = calculate_recovery_score(df)

    # Return the final processed DataFrame
    return df

