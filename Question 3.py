#Online Store Shipping Fee:
#Write a program for an online store that tells you shipping fees based on the order total (entered via user input):

#If the order total is less than $50, the shipping fee is $10.
#If the order total is between $50 and $100, the shipping fee is $5.
#If the order total is above $100, shipping is free.

#Expected Output:
#Enter your order total: 76
#Shipping fee: $5

total_orders=int(input("Enter your order total:"))
if total_orders >100:
    print("You got free shipping")
elif total_orders >=50 and total_orders<100:
    print("Shipping fee: $5")
elif total_orders <50:
    print("Shipping fee: $10")
else:
    print("Warning! WRONG INPUT")