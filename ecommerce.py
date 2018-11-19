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
