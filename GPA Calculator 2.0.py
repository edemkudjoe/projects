from tabulate import tabulate

maindata = []

print("GPA CALCULATOR 2.0")
name = input("Enter your name: ")
university = input("Enter the name of your institution: ")
level = input("Enter your level: ")
faculty = input("What faculty do you belong to? \n")
program = input("Enter your programme: ")

print("Please confirm your name and Level: ")
print(f"Name: {name}")
print(f"Level: {level}")
print(f"University: {university}")
print(f"Faculty: {faculty}")
print(f"Program: {program}")

confirm = input("Type 'Yes' to confirm: ")
if confirm.lower() != "yes":
    print("Try again.")
    exit()  

print("GPA CALCULATOR 2.0 PART 2")

maindata = []

number_of_courses = int(input("Enter the number of courses you are doing this semester: \n"))
while number_of_courses > 10:
    print("Entry limit reached, try again")
for i in range(number_of_courses):
    Course = input("Enter your course: ")
    Grade = input("Enter your Course grade: ")
    Credits = int(input(f"Enter the credit hours permitted for {Course}: \n"))
    GPA = 0.0
    finalGPA = 0
    finalCreditHours = 0
    if 80 <= int(Grade) <= 100:
        GPA = 4.0
        LGrade = "A"
        Interpretation = "Excellent"
    elif 75 <= int(Grade) <= 79:
        GPA = 3.5
        LGrade = "B+"
        Interpretation = "Very Good"
    elif 70 <= int(Grade) <= 74:
        GPA = 3.0
        LGrade = "B"
        Interpretation = "Good"
    elif 65 <= int(Grade) <= 69:
        GPA = 2.0
        LGrade = "B-"
        Interpretation = "Above Average"
    elif 60 <= int(Grade) <= 64:
        GPA = 1.0
        LGrade = "C+"
        Interpretation = "Average"
    elif 55 <= int(Grade) <= 59:
        GPA = 0.0
        LGrade = "C"
        Interpretation = "Below Average"
    elif 50 <= int(Grade) <= 54:
        GPA = 0.0
        LGrade = "C-"
        Interpretation = "Marginal Pass"
    elif 45 <= int(Grade) <= 49:
        GPA = 0.0
        LGrade = "D"
        Interpretation = "Unsatisfactory"
    elif 0 <= int(Grade) <= 44:
        GPA = 0.0
        LGrade = "F"
        Interpretation = "Fail"
    else:
        GPA = 0.0
        LGrade = "X"
        Interpretation = "Absent"
    maindata.append([Course, Credits, LGrade, GPA, Interpretation])
    finalGPA += GPA
    finalCreditHours += Credits
    calculatedGPA = finalGPA/finalCreditHours

maindata.append(["","","Final GPA", round(calculatedGPA, 2)])

headers = ["Course","Credits","Grade","GPA", "Interpretation"]

table = tabulate(maindata, headers, tablefmt="grid")

print(f"Name: {name}")
print(f"Level: {level}")
print(f"University: {university}")
print(f"Faculty: {faculty}")
print(f"Program: {program}")
print(table)

print(f"Your final GPA is {calculatedGPA}")
exit()
