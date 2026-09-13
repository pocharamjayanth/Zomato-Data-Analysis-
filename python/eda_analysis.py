import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv("data/cleaned/zomato_cleaned.csv")
os.makedirs("images/charts", exist_ok=True)

print("--- 1. RESTAURANT TYPES DISTRIBUTION ---")
type_counts = df['listed_in(type)'].value_counts()
print(type_counts)

print("\n--- 2. ONLINE ORDER ADOPTION (%) ---")
online_pct = df['online_order'].value_counts(normalize=True) * 100
print(online_pct)

print("\n--- 3. AVERAGE RATING BY RESTAURANT TYPE ---")
avg_rating = df.groupby('listed_in(type)')['rate'].mean()
print(avg_rating)

print("\n--- 4. STATISTICAL SUMMARY ---")
print(df[['rate', 'votes', 'approx_cost(for two people)']].describe())

# Generate basic plots and save them
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='listed_in(type)')
plt.title('Restaurant Distribution by Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/charts/restaurant_types.png')
plt.close()

print("\nEDA script completed successfully and charts saved to images/charts/!")
