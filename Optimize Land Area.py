#!/usr/bin/env python
# coding: utf-8

# In[32]:


from scipy.optimize import linprog
from InferenceModel import infer
from growthTime import crop_to_time_dict
from averageArea import crop_to_area_dict

top_crops, probs = infer()

time_to_grow = [crop_to_time_dict[crop] for crop in top_crops]
output_per_area = [crop_to_area_dict[crop] for crop in top_crops]

"""
Top crops will be a list where each item of this list will be a key to the dictionary we will make
"""

def allocate_optimal_land():
    """
    
    Arguments : top_crops, current_money, buying_price, selling_price, output_per_area, time_to_grow
    
    Returns : Optimal allocation of land to each crop
    
    General Notes : 
    
    top_crops : Name crops with highest probability, a list. Each element of this list is a key for the dictionary.
    current_money : integer 
    buying_price : current price 
    selling_price : forecasted price
    output_per_area : dictionary for each crop
    time_to_grow : dictionary for each crop
    
    """
    current_money = 70
    buying_price = [4,6,7,80,5]
    price_per_kg = [10, 8, 12, 99, 9]
    output_per_area = [0.5, 4, 2, 4, 7]
    time_to_grow = [10, 4, 2, 1, 6]
    max_time_to_grow = max(time_to_grow) 

    scaled_growth = [max_time_to_grow//x for x in time_to_grow]
    total_land_area = 15

    c = [-(price_per_kg[i]*scaled_growth[i]*output_per_area[i]) for i in range(len(time_to_grow))]

    A_eq = [[1, 1, 1, 1, 1], [buying_price[i]*output_per_area[i] for i in range(len(buying_price))]]

    b_eq = [total_land_area, current_money]

    bounds = [(0, total_land_area) for _ in range(5)] 

    available_land = total_land_area

    b_eq[0] = available_land

    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    land_allocation = result.x[:5]

    for j, allocation in enumerate(land_allocation):
        print(f"Allocate {allocation:.2f} units of land to Crop {j + 1}")


# In[33]:


allocate_optimal_land()

