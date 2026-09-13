import pandas as pd
import sqlite3
import os

# Load cleaned dataset
df = pd.read_csv("data/cleaned/zomato_cleaned.csv")

# Create an in-memory or local SQLite database connection
conn = sqlite3.connect("data/zomato.db")
cursor = conn.cursor()

# Load dataframe into a SQL table
df.to_sql("zomato_restaurants", conn, if_exists="replace", index=False)

print("--- SQL QUERY 1: Top 5 Highest Rated Restaurants ---")
query_1 = """
    SELECT name, rate, votes, location, 'approx_cost(for two people)' as cost
    FROM zomato_restaurants
    WHERE rate IS NOT NULL
    ORDER BY rate DESC, votes DESC
    LIMIT 5;
"""
print(pd.read_sql(query_1, conn))

print("\n--- SQL QUERY 2: Average Cost and Rating by Restaurant Type ---")
query_2 = """
    SELECT "listed_in(type)" as restaurant_type, 
           COUNT(*) as total_restaurants,
           ROUND(AVG(rate), 2) as avg_rating,
           ROUND(AVG("approx_cost(for two people)"), 2) as avg_cost
    FROM zomato_restaurants
    GROUP BY "listed_in(type)"
    ORDER BY avg_rating DESC;
"""
print(pd.read_sql(query_2, conn))

# Close connection
conn.close()
print("\nSQL analysis completed and database stored at data/zomato.db!")
