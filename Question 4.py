#Returning Total Salary Information for a Job:
#You have a base salary as well as a dictionary with job titles and associated bonus rates. Write a program that takes a job title as user input and:

#first checks if that job title is in the dictionary (hint: use in keyword).
#if it is, the program returns the final total salary for the job (base + bonus)
#if it is not in the dictionary, it returns "salary information for this job not available"

#Expected Output:
#Enter your job title: project manager
#Final salary is 115000.0


#Enter your job title: hr manager
#Salary information for this job not available

bonuses = {"product manager" : 0.1, "project manager" : 0.15, "marketing manager" : 0.2}
base_salary = 100000
job_title=str(input("Enter job title: "))
if job_title in bonuses.keys():
    print("Final salary is ", (base_salary*bonuses[job_title]+base_salary))
else:
    print("salary information for this job not available")