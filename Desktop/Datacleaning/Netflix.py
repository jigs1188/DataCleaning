
import pandas as pd
import numpy as np

# Load the data
data = pd.read_csv('/home/jigs/Desktop/Datacleaning/netflix1.csv')

# Display basic information about the dataset
print("Initial Data Info:")
print(data.info())
print("\nInitial Data Description:")
print(data.describe())
print("\nInitial Data Sample:")
print(data.head())

# Handling missing values
# Fill missing values in 'rating' and 'country' with 'Unknown'
data['rating'] = data['rating'].fillna('Unknown')
data['country'] = data['country'].fillna('Unknown')

# Fill missing values in 'date_added' with mode
data['date_added'] = data['date_added'].fillna(data['date_added'].mode()[0])

# Removing duplicates
data = data.drop_duplicates()

# Standardizing data formats
# Convert 'date_added' to datetime format
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')

# Convert 'title' to lower case
data['title'] = data['title'].str.lower()

# Save the cleaned data to a new CSV file
data.to_csv('cleaned_netflix_titles.csv', index=False)

print("Data cleaning complete. Cleaned data saved to 'cleaned_netflix_titles.csv'.")
