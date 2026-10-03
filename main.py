print("Student Marks Calculator")

name = input("Enter student name: ")

mark1 = int(input("Enter mark for Subject 1: "))
mark2 = int(input("Enter mark for Subject 2: "))
mark3 = int(input("Enter mark for Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
