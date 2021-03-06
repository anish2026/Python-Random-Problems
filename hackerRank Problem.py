#The following code is the part of the hackerrank 30 day challenge.

#!/bin/python3 
 
import math 
import os 
import random 
import re 
import sys 
 
# 
# Complete the 'solve' function below. 
# 
# The function accepts following parameters: 
#  1. DOUBLE meal_cost 
#  2. INTEGER tip_percent 
#  3. INTEGER tax_percent 
# 
 
def solve(meal_cost, tip_percent, tax_percent): 
    return round(meal_cost + (tip_percent*meal_cost)/100 + (tax_percent*meal_cost)/100) 
 
if name == '__main__': 
    meal_cost = float(input().strip()) 
 
    tip_percent = int(input().strip()) 
 
    tax_percent = int(input().strip()) 
 
    print(solve(meal_cost, tip_percent, tax_percent))
