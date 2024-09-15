import pandas as pd

filename = r'C:\Users\Jinesh\OneDrive\Desktop\DV1\GreenMetric\GreenMetric_2016-.csv'

df = pd.read_csv(filename)

# Add the 'Year' column with a fixed value
df['Year'] = 2016  # Set the desired year value

df.to_csv(filename, index=False)

print("Year column added successfully!")
