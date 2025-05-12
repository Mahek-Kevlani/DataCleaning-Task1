import pandas as pd

# Load the dataset
df = pd.read_csv('dataset.csv')  

# Print original column names for debugging
print("Original Columns:", df.columns)

# Convert all column names to lowercase and replace spaces with underscores
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Handle missing values using forward fill
df = df.ffill()  # or use df.dropna() if you prefer to drop rows

# Remove duplicates
df = df.drop_duplicates()

# Standardize the 'gender' column
df['gender'] = df['gender'].str.lower().str.strip()

# Convert scheduled and appointment dates to datetime format
df['scheduledday'] = pd.to_datetime(df['scheduledday'], errors='coerce')
df['appointmentday'] = pd.to_datetime(df['appointmentday'], errors='coerce')

# Ensure 'age' is an integer
df['age'] = df['age'].astype(int)

# Save cleaned dataset
df.to_csv('cleaned_dataset.csv', index=False)

print("\n Data cleaning completed and saved as 'cleaned_dataset.csv'.")


