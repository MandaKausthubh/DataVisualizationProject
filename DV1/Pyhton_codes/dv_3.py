# Uniforming the countries column in GreenMetrics

import pandas as pd

file_path = r"C:\Users\Jinesh\OneDrive\Desktop\DV1\GreenMetric\GreenMetric_2016-.csv"
df = pd.read_csv(file_path)

# Replacing 'United States' with 'USA' and 'United Kingdom' with 'UK' in the 'Country' column
df['Country'] = df['Country'].replace({
    'United States': 'USA',
    'United Kingdom': 'UK'
})


output_path = file_path
df.to_csv(output_path, index=False)

print("Country names updated successfully!")
