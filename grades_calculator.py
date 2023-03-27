# Define a function to calculate the average grade
def calculate_average_grade(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

#Get the number of students
num_students = int(input("How many students do you want to enter? "))

#Create two empty dictionaries
grades_dict = dict()
mean_dict = dict()

for i in range(num_students):
    #Get the student name
    student = input("Enter the student #" + str(i+1) + " name: ")

    # Get the number of grades
    num_grades = int(input("How many grades do you want to enter? "))

    # Get the grades from the user
    grades = []
    for i in range(num_grades):
        grade = float(input("Enter grade #" + str(i+1) + ": "))
        grades.append(grade)

    # Calculate the average grade
    average_grade = calculate_average_grade(grades)

    #Append the values to each dict
    grades_dict[student] = grades
    mean_dict[student] = average_grade

print( "The students grades are: ")
print(grades_dict)
print( "The mean for student: ")
print(mean_dict)