#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 11:51:08 2018

@author: hannaholdorf
"""

#%%
#Create a function named checkout that takes a list that represents a shopping cart and returns the total cost of it. 
#This function should check that the shopping cart must not be empty.


prices = []

product = {"guitar":1000, "box":5, "strings":10}

def checkout(shopping_cart):
    if shopping_cart == []:
        return "Your shopping cart is empty, please add an item to your cart"
    else:
        for items in shopping_cart:
            prices.append(product[items])
   
    return sum(prices)


#checkout(["strings","strings"])

#%%

prices2 = []

product2 = {"guitar":1000, "box":5, "strings":10}
addproducts = {"insurance":5, "priority":10}


    def checkout2(shopping_cart, insurance, priority):
    
    if shopping_cart == []:
        return "Your shopping cart is empty, please add an item to your cart"
    else: 
        for items in shopping_cart:
            prices2.append(product2[items])

        if insurance == "yes":
            prices2.append(addproducts["insurance"])
        
        if priority== "yes":
            prices2.append(addproducts["priority"])
    
    return sum(prices2)


#checkout2(["guitar"], "yes", "yes")


#%% 
    
class Product:
    
    def _init_(self, name, price):
        self.name = name
        self.price = price

class Service:
    
    def _init_(self,name, price):
        self.name = name
        self.price = price

class Tier:
    
    def _init_(self, name):
        self.name = name

    def discount(self, item):
        if self.name == "gold":
            return 0.95 * item.price 
        elif self.name == "silver":
            if isinstance(item, Product):       #isinstance reffering if item is part of (intance) of class Product
                return 0.98 * item.price
            else:
                return item.price
        else:
            return item.price



cart = [
        Product("guitar", 1000),
        Product("pick box", 5),
        Product("strings", 10),
        Service("insurance", 5),
        Service("priority", 10)
        ]


normal_tier = Tier("normal")
silver_tier = Tier("silver")
gold_tier = Tier("gold")


def checkout3(shopping_cart, tier=normal_tier):
    
    if shopping_cart == []:
        return "Your shopping cart is empty, please add an item to your cart"
        return None
    
    total = 0
    
    services_in_cart = set()
    
    for item in shopping_cart:
        
        if isinstance(item, Service):
            if item.name in Service in cart:
                continue 
            else:
                services_in_cart.add(item.name)
        
        total += tier.discount(item)
    
  #  for item in shopping_cart:
  #      total += item.price(Product)
    
    
    
    return total

