"""
Xiyao Huang
202306631
x2023fkv@stfx.ca

Rename the 'class' into 'target',
Make the target class into the new binary class.
"""

import pandas as pd

# File paths
input_path = r'C:\Users\raymo\OneDrive\Desktop\Phase4\Data1107.csv'
output_path = r'C:\Users\raymo\OneDrive\Desktop\TabularPhase4\DataSecond.csv'

# Load the data
df = pd.read_csv(input_path)

# Delete the specified columns
df.drop(columns=['Genotype', 'Treatment', 'Behavior'], inplace=True)

# Print unique values in the 'class' column before mapping
print("Unique values in 'class' column before mapping:")
print(df['class'].unique())

# Update the class column based on the specified rules
class_mapping = {
    'b\'c-SC-s\'': '0',
    'b\'c-SC-m\'': '0',
    'b\'t-SC-s\'': '0',
    'b\'t-SC-m\'': '0',
    'b\'t-CS-s\'': '0',
    'b\'c-CS-s\'': '1',
    'b\'c-CS-m\'': '1',
    'b\'t-CS-m\'': '1'
}

# Convert 'class' column to string and apply mapping
df['class'] = df['class'].astype(str).map(class_mapping)

# Print unique values in the 'class' column after mapping
print("Unique values in 'class' column after mapping:")
print(df['class'].unique())

# Rename the 'class' column to 'target'
df.rename(columns={'class': 'target'}, inplace=True)

# Save the updated DataFrame to a new CSV file
df.to_csv(output_path, index=False)

print(f"Data processed successfully and saved to {output_path}")
