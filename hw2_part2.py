# File: hw2_part2.py
# Author: Uzoma Uwanamodo
# Date: 9/19/2016
# Section: 04
# E-mail: uu3@umbc.edu
# Description:
# Resolves a float value into dollars and cents
# Collaboration:
# I did not collaborate with anyone on this assignment

def main():
    PRICE_TO_CENTS = 100 # Amount to multiply price float value by to get cents amount
    print("What is the price?")
    price = float(input()) # Ask for the price
    dollars = int(price) # Resolve the price into dollar component
    cents = int((price-dollars)*PRICE_TO_CENTS) # Resolve the price into cents component
    print("The number of dollars is: %s\nThe number of cents is: %s" % (dollars, cents))
    
main()