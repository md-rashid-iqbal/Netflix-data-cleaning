import pandas as pd

# 1. Load the dataset
# We use pd.read_csv to open the raw data file downloaded from Kaggle
try:
    df = pd.read_csv('netflix_data.csv')
    print("Success: Dataset loaded successfully.")

    # 2. Handling Missing Values (Data Cleaning)
    # Some columns like director and cast have empty cells (NaN). 
    # We fill them with 'Unknown' to maintain data consistency.
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df['country'] = df['country'].fillna('Unknown')

    # Drop rows where critical information like 'date_added' or 'rating' is missing
    # These are very few rows, so removing them won't affect the overall analysis.
    df.dropna(subset=['date_added', 'rating', 'duration'], inplace=True)
    # 4. Standardizing Column Headers
    # Converting all column names to lowercase and replacing spaces with underscores
    # This makes it easier to write code without worrying about capital letters.
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]

    # 5. Removing Duplicates
    # Checking and removing any duplicate rows to ensure data quality.
    df.drop_duplicates(inplace=True)

    # 6. Saving the Cleaned Dataset
    # We save the final processed data into a new CSV file for submission.
    df.to_csv('cleaned_netflix_data.csv', index=False)
    print("Success: Cleaned data saved as 'cleaned_netflix_data.csv'.")

except FileNotFoundError:
    print("Error: The file 'netflix_data.csv' was not found in the folder.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
