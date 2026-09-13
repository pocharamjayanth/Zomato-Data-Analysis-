import pandas as pd
import os

# Load cleaned dataset
df = pd.read_csv("data/cleaned/zomato_cleaned.csv")
os.makedirs("excel", exist_ok=True)

# Create a pivot table summarizing restaurant metrics by location and type
pivot_df = pd.pivot_table(
    df,
    index=['location'],
    columns=['listed_in(type)'],
    values='rate',
    aggfunc=['count', 'mean'],
    fill_value=0
)

# Flatten columns for clean export
pivot_df.columns = [f'{col[0]}_{col[1]}' for col in pivot_df.columns]
pivot_df = pivot_df.reset_index()

# Save the pivot summary for Excel reporting
output_path = "excel/zomato_summary_pivot.csv"
pivot_df.to_csv(output_path, index=False)

print(f"Excel summary pivot table successfully generated and saved to {output_path}!")
print(pivot_df.head())
