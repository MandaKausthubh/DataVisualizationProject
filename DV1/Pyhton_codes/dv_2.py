import pandas as pd

# NatureIndex

file_path = r"C:\Users\Jinesh\OneDrive\Desktop\DV1\NatureIndex\NatureIndex_2022.csv"  # Replace with the actual file path
df = pd.read_csv(file_path)

# Rename the columns
df.rename(columns={
    '2022': 'World Rank',
    'Share 2022': 'Share',
    'Count 2022': 'Count'
}, inplace=True)

# Remove commas from the 'Count' column and convert to numeric
df['Count'] = df['Count'].str.replace(',', '').astype(float)

# Add 'Year' column with a fixed value
df['Year'] = 2022

# Calculate 'Publication share' (Count / total Count)
total_count = df['Count'].sum()
df['Publication share'] = (df['Count'] / total_count) * 100

# Handle splitting of University and Country
df[['Institution', 'Country']] = df['Institution'].str.rsplit(', ', n=1, expand=True)

output_path = r"C:\Users\Jinesh\OneDrive\Desktop\DV1\NatureIndex\Updated_NatureIndex_2021.csv"  # Saving to a new file to avoid overwriting
df.to_csv(output_path, index=False)

print("File updated and saved successfully!")
