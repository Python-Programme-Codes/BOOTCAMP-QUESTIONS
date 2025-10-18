#Compounding Discount:
#You have a base price for a product. Write a program that calculates final price after discount. The program should:

#check if member is set to 1 and should cut the price by 25% if yes.
#it should then check if woman is set to 1 and cut the already reduced price further by 15% if yes
#it should then check if senior_citizen is set to 1 and cut the remaining price further by 10% if yes

#price = 1000

#member = 1
#woman = 1
#senior_citizen = 1

#Expected Output: The final price is 573.75


#price = 1000

#member = 1
#woman = 0
#senior_citizen = 1

#Expected Output: The final price is 675.0

price = 1000

member = 1
woman = 0
senior_citizen = 1
if member == 1:
    price = price - (price * 0.25)
if woman == 1:
    price = price - (price * 0.15)
if senior_citizen == 1:
    price = price - (price * 0.10)

print("The final price is", price)
