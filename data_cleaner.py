import pandas as pd

# Load the CSV file (change path if needed)
df = pd.read_csv('addresses.csv')  # In Replit/Colab, upload the file first

# Show original data
print("Original Data:")
print(df.head())

# Clean and transform
df_clean = df.dropna()  # Remove rows with missing values
df_clean['Full Name'] = df_clean['First'] + ' ' + df_clean['Last']  # Combine names

# Summary stats
print("\nSummary:")
print(f"Total records after cleaning: {len(df_clean)}")
print(f"Unique cities: {df_clean['City'].nunique()}")

# Save cleaned version
df_clean.to_csv('cleaned_addresses.csv', index=False)
print("\nCleaned file saved as 'cleaned_addresses.csv'")
