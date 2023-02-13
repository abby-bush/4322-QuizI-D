"""
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
"""

import csv

# open the file
infile = open("employee_data.csv", "r")
reader = csv.reader(infile, delimiter=",")


# create an empty dictionary
employees = {}


# use a loop to iterate through the csv file
for row in reader:
    # check if the employee fits the search criteria
    if row[3] == "Marketing":
        if row[4] == "CSR":
            # consolidating first names and last names
            fname = row[1]
            lname = row[2]
            name = fname + " " + lname

            # calculating future salary
            current_salary = float(row[5])
            future_salary = round(float(current_salary) * 1.1, 2)

            # adding information to the dictionary
            employees[name] = future_salary

            # printing current salary per printout instructions
            print(
                f"Manager Name: {name} Current Salary: ${format(current_salary, ',.2f')}"
            )


print()
print("=========================================")
print()


# iternate through the dictionary and print out the key and value as per printout
for i in employees:
    print(f"Manager Name: {i} New Salary: ${format(employees[i], ',.2f')}")
