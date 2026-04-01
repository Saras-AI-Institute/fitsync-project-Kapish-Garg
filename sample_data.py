import pandas as pd

def main():
    # Load the CSV file
    file_path = 'data/health_data.csv'
    health_data = pd.read_csv(file_path)

    # Print the first 5 rows
    print('First 5 rows:')
    print(health_data.head())

    # Print the number of missing values in each column
    print('\nNumber of missing values in each column:')
    print(health_data.isnull().sum())

if __name__ == "__main__":
    main()
