import numpy as np
import random

class UtilityBasedAgent:
    def __init__(self, browsing_his, purchase_his, products):
        self.browsing_his = browsing_his 
        self.purchase_his = purchase_his 
        self.products = products 
    
    def calculate_utility(self, product):
        rating = random.uniform(0, 1)  
        discount = random.uniform(0, 1)  
        browsing = 0.2
        purchase = 0.1
        
        rating_score = product.get('rating', 0) / 5  
        discount_score = product.get('discount', 0) / 100  
        browsing_score = 1 if product['id'] in self.browsing_his else 0
        purchase_score = 1 if product['id'] in self.purchase_his else 0
        
        utility = (
            rating * rating_score +
            discount * discount_score +
            browsing * browsing_score +
            purchase * purchase_score
        )
        return utility
    
    def suggestion(self, top_n=5):
        scored_products = [(product, self.calculate_utility(product)) for product in self.products]
        scored_products.sort(key=lambda x: x[1], reverse=True)  
        return [product for product, score in scored_products[:top_n]]

browsing_his = [101, 102, 103]
purchase_his = [102]
products= [
    {'id': 101, 'name': 'Laptop', 'rating': 4.5, 'discount': 10},
    {'id': 102, 'name': 'Smartphone', 'rating': 4.8, 'discount': 15},
    {'id': 103, 'name': 'Headphones', 'rating': 4.2, 'discount': 5},
    {'id': 104, 'name': 'Smartwatch', 'rating': 4.0, 'discount': 20},
    {'id': 105, 'name': 'Tablet', 'rating': 3.8, 'discount': 25}
]

agent = UtilityBasedAgent(browsing_his, purchase_his, products)
suggestions = agent.suggestion()

for product in suggestions:
    print(f"Suggested: {product['name']} (Rating: {product['rating']}, Discount: {product['discount']}%)")  
