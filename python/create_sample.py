import pandas as pd
import numpy as np

data = {
    'name': ['Restaurant A', 'Cafe B', 'Dining C', 'Dine D', 'Cafe E', 'Restaurant F', 'Bar G', 'Buffet H', 'Cafe I', 'Dining J'],
    'online_order': ['Yes', 'yes', 'No', 'no', 'Yes', 'No', 'Yes', 'no', 'yes', 'Yes'],
    'book_table': ['Yes', 'No', 'Yes', 'no', 'No', 'Yes', 'no', 'yes', 'no', 'Yes'],
    'rate': ['4.1/5', '3.8/5', 'NEW', '4.5/5', '-', '3.2/5', '4.0/5', '3.9/5', '4.2/5', '3.5/5'],
    'votes': [120, 85, 0, 450, 12, 60, 310, 220, 150, 95],
    'location': ['Koramangala', 'Indiranagar', 'BTM', 'Jayanagar', 'Koramangala', 'Indiranagar', 'MG Road', 'BTM', 'Koramangala', 'Jayanagar'],
    'rest_type': ['Casual Dining', 'Cafe', 'Casual Dining', 'Fine Dining', 'Cafe', 'Quick Bites', 'Bar', 'Casual Dining', 'Cafe', 'Casual Dining'],
    'cuisines': ['North Indian, Chinese', 'Cafe, Fast Food', 'South Indian', 'Italian, Continental', 'Beverages, Desserts', 'South Indian', 'Finger Food, North Indian', 'North Indian, Mughlai', 'Coffee, Tea', 'Biryani, Chinese'],
    'approx_cost(for two people)': ['600', '400', '1,200', '2,500', '300', '250', '1,500', '1,000', '350', '800'],
    'listed_in(type)': ['Buffet', 'Cafes', 'Delivery', 'Dine-out', 'Cafes', 'Delivery', 'Pubs and bars', 'Buffet', 'Cafes', 'Dine-out']
}

df = pd.DataFrame(data)
df.to_csv('zomato.csv', index=False)
print('Sample zomato.csv created successfully!')
