# Student Marks Calculator

def calculate_result(marks):

    total = sum(marks)
    average = total / len(marks)

    print("\n===== STUDENT RESULT =====")
    print("Total Marks:", total)
    print("Average Marks:", average)

    if average >= 90:
        print("Grade: A")
    elif average >= 75:
        print("Grade: B")
    elif average >= 50:
        print("Grade: C")
    else:
        print("Grade: D")


name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input("Enter marks for subject " + str(i) + ": "))
    marks.append(mark)

print("\nStudent Name:", name)

calculate_result(marks)