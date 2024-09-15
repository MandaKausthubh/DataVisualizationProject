# making Times data relevant ot our work

import pandas as pd

file_path = r"C:\Users\Jinesh\OneDrive\Desktop\DV1\Times\Times_2016.csv"
df = pd.read_csv(file_path)

# Remove specified columns
columns_to_remove = ['record_type', 'member_level', 'url', 'nid', 'stats_female_male_ratio',
                     'aliases', 'closed', 'unaccredited', 'disabled', 'rank_order']
df = df.drop(columns=columns_to_remove)

df['year'] = 2016

output_file_path = file_path
df.to_csv(output_file_path, index=False)

print("File processed and saved as", output_file_path)
