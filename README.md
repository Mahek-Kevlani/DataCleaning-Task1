Data Cleaning Process
This repository contains Python scripts for cleaning and preprocessing datasets. Below are the steps involved in the data cleaning process.

Steps for Data Cleaning

1. Identify and Handle Missing Values
     Use `.isnull()` to identify missing values and handle them by either filling or dropping them.
     import pandas as pd
     df = pd.read_csv('data.csv')
     df.isnull().sum()  # Count missing values in each column
     df.fillna('Unknown', inplace=True)  # Fill with a default value
     df.dropna(inplace=True)  # Drop rows with missing values
     
 2. Remove Duplicate Rows
     Use `.drop_duplicates()` to remove duplicate rows from the dataset.
     df.drop_duplicates(inplace=True)
   
 3. Standardize Text Values
     Standardize values like gender, country names, etc., by using string operations.
     df['gender'] = df['gender'].str.lower().replace({'male': 'M', 'female': 'F'})
     df['country'] = df['country'].str.title()  # Capitalize each word
    
 5. Convert Date Formats
     Convert date columns to a consistent format using `pd.to_datetime()`.
     python
     df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

 6. Rename Column Headers
     Rename columns to make them clean and consistent.
     python
     df.columns = df.columns.str.lower().str.replace(' ', '_')
     
  7. Check and Fix Data Types
     Ensure data types are correct using astype(). For example, converting the 'age' column to integer and 'date' column to datetime.
     python
     df['age'] = df['age'].astype(int)
     df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')




