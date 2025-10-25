#Passing Students (10 Marks)
#Given the dictionary below, write a function that takes in a
# dictionary and returns the names of
# all the students who passed (i.e. had 70 marks or above) as well as their grade:

#70-80 - C
#80-90 - B
#90-100 - A
#Sample Output:

#Ali passed with B grade
#Sara passed with A grade
#Zara passed with B grade

def student_grade(score):
    for key, value in student_marks.items():
        if value >= 90 and value < 100:
            print(key, "passed with A grade")
        elif value >= 80 and value < 90:
            print(key, "passed with B grade")
        elif value >= 70 and value < 80:
            print(key, "passed with C grade")



student_marks = {
    'Ali': 85,
    'Sara': 92,
    'Ahmed': 56,
    'Zara': 89,
    'Bilal': 67,
    'Hina': 81,
    'Omar': 90,
    'Nida': 63,
    'Usman': 78,
    'Fatima': 95
    }

student_grade(student_marks)