"""
Create a program that calculates the price of a movie ticket based on the age of the customer. If the customer is under 12, the ticket costs $5; if they are between 12 and 65, the ticket costs $10; otherwise, it's $7.
"""
customer_age = float(input("Enter the age of customer: "))
if 0 < customer_age <= 65:
    if customer_age < 12:
        print("The price of ticket is $5")
    else:
        print("The price of ticket is $10")
else:
    print("the price of ticket is $7")
