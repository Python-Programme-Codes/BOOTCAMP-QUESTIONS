#Grade Checker:
#Write a program that takes a student's marks (out of 100) as user input and prints their grade based on the following criteria:

#90-100: A
#80-89: B
#70-79: C
#60-69: D
#Below 60: Fail

#Expected Output

#Enter your marks (out of 100): 76
#Your grade is: C

marks=int(input("Enter your marks (out of 100): "))
if marks >=90 and marks<100:
    print("Your grade is: A")
elif marks >=80 and marks<90:
    print("Your grade is: B")
elif marks >=70 and marks<80:
    print("Your grade is: C")
elif marks >=60 and marks<70:
    print("Your grade is: D")
elif marks <60:
    print("Your grade is: F")
else:
    print("Invalid input.")
