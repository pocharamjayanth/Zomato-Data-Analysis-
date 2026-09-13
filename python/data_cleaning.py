import pandas as pd
import numpy as np
import os

# 1. Load the dataset from the root directory
if os.path.exists("zomato.csv"):
    df = pd.read_csv("zomato.csv")
else:
    raise FileNotFoundError("zomato.csv is not found in the root Zomato-Data-Analytics folder. Please place it there.")

print(f"Original Dataset Shape: {df.shape}")

# 2. Drop duplicate rows
print(f"Duplicate rows detected: {df.duplicated().sum()}")
df = df.drop_duplicates()

# 3. Clean the 'rate' column
def clean_rating(value):
    value = str(value).strip()
    if value in ['NEW', '-', 'nan', 'None']:
        return np.nan
    try:
        return float(value.split('/')[0])
    except:
        return np.nan

df['rate'] = df['rate'].apply(clean_rating)

# 4. Clean the 'approx_cost(for two people)' column
df['approx_cost(for two people)'] = (
    df['approx_cost(for two people)']
    .astype(str)
    .str.replace(',', '', regex=False)
)
df['approx_cost(for two people)'] = pd.to_numeric(
    df['approx_cost(for two people)'], 
    errors='coerce'
)

# 5. Standardize text columns
df['online_order'] = df['online_order'].astype(str).str.strip().str.lower()
df['book_table'] = df['book_table'].astype(str).str.strip().str.lower()
df['listed_in(type)'] = df['listed_in(type)'].astype(str).str.strip()

# 6. Save the cleaned dataset
os.makedirs("data/cleaned", exist_ok=True)
df.to_csv("data/cleaned/zomato_cleaned.csv", index=False)

print(f"Cleaned Dataset Shape: {df.shape}")
print("Data cleaning executed successfully! Saved to data/cleaned/zomato_cleaned.csv")