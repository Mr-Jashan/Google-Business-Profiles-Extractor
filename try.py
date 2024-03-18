import pandas as pd
import os
import csv

# Assuming you have already imported pandas and os modules

df = pd.read_csv('data.csv')

csv_file_path = os.path.expanduser('./data.csv')

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Name', 'Rating', 'Address', 'Phone No', 'Plus code', 'Link'])
    for _, row in df.iterrows():
        phone_no = row['Phone No'] if not pd.isna(row['Phone No']) else ''
        writer.writerow([row['Name'], row['Rating'], row['Address'], phone_no, row['Plus code'], f'=HYPERLINK("{row["Link"]}", "{row["Link"]}")'])
