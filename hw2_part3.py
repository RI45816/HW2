# File: hw2_part3.py
# Author: Uzoma Uwanamodo
# Date: 9/19/2016
# Section: 04
# E-mail: uu3@umbc.edu
# Description:
# Create a rudimentary shopping list
# Collaboration:
# I did not collaborate with anyone on this assignment

def main():
    totalNumber = 0
    item1 = input("What would you like to buy first? ") # Ask user for first item
    
    if item1 != "":
        totalNumber += 1
        print("You are buying %s" % item1)
        amount1 = int(input("How many would you like to buy? ")) # Ask user for amount of first item
        
        
        
        # Get info for second item
        item2 = input("What would you like to buy second? ")
                
        if item2 != "":
            totalNumber += 1    
            print("You are buying %s" % item2)
            amount2 = int(input("How many would you like to buy? "))
        
            # Get info for third item
            item3 = input("What would you like to buy third? ")
            if item3 != "":
                totalNumber += 1
                print("You are buying %s" % item3)
                amount3 = int(input("How many would you like to buy? "))
                
                
    print("You are buying %s items:\n%s %s\n%s %s\n%s %s" % (totalNumber, item1, amount1, item2, amount2, item3, amount3))
main()