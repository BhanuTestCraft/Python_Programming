"""
Write a program to calculate bill. Ask the fi nal amount from the user.
You have to give discount and print the fi nal bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount
Print the discount and the fi nal amount to be paid.

Example 1
Enter bill amount = 80000
You got 30% discount
Your fi nal bill is Rs. 56000
"""
bill_amount = float(input("Enter the bill amount= "))
if bill_amount >= 50000:
    discount = 30
elif bill_amount >= 40000 and bill_amount < 50000:
    discount = 25
elif bill_amount >= 30000 and bill_amount < 40000:
    discount = 20
elif bill_amount >= 20000 and bill_amount < 30000:
    discount = 10
else:
    discount = 0
print(f"you got discount of {discount}%")
final_bill_amount = (bill_amount) - ((discount * bill_amount) / 100)
print(f"Your final bill is Rs. {final_bill_amount:.2f}")
