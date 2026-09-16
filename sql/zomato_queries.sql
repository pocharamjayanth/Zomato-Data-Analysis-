-- Query 1: Top Highest Rated Restaurants
SELECT name, rate, "approx_cost(for two people)" AS cost
FROM zomato
ORDER BY rate DESC
LIMIT 5;

-- Query 2: Average Cost and Rating by Restaurant Type
SELECT 
    "listed_in(type)" AS restaurant_type,
    AVG(rate) AS avg_rating,
    AVG("approx_cost(for two people)") AS avg_cost
FROM zomato
GROUP BY "listed_in(type)";
