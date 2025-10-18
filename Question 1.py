#Currency Converter:
#Create a program where the user inputs an amount in USD,
#and the program converts it to Euros (use an exchange rate of 1 USD = 0.85 EUR).
#The output should show "___ USD is equal to ___ Euro"


#Expected output:

#Enter your amount in USD: 100
#100 USD is equal to 85 Euros

amount = int(input("Enter your amount in USD: "))
exchange = amount * 0.85
print(amount,"USD is equal to ",exchange,"Euros")