# File: hw2_part1.py
# Author: Uzoma Uwanamodo
# Date: 9/19/2016
# Section: 04
# E-mail: uu3@umbc.edu
# Description:
# Calculates the total cost to buy and ship a large order of books from the bookstore
# Collaboration:
# I did not collaborate with anyone on this assignment



def main():
    SHIPPING_PRICE = 6.95
    TAX_MULTIPLIER  = 1.06 # How much to multiply the subtotal by to get the total plus tax (100% + 6% = 1 + .06 = 1.06)
    print("What is the price of the book?")
    price = float(input()) # Get the price of the book
    print("How many copies do you want")
    quantity = int(input(), 10) # Get the amount of copies of the book
    subtotal = price * quantity # Get subtotal price by multiplying the price and quantity
    shipping = quantity * SHIPPING_PRICE # Determine how much shipping costs
    total = subtotal * TAX_MULTIPLIER + shipping # Get the total amount, with subtotal plus tax and shipping
    print("The total cost is $%.2f" % total)

main()