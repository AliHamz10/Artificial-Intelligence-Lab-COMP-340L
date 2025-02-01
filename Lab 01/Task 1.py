"""
Dictionary Manipulation
# 1.1 Create a dictionary representing a student's information with keys like 'name', 'age', 'grade',
# and 'subjects'. Perform the following operations:
# 1.2 Add a new subject to the 'subjects' list.
# 1.3 Update the student's age.
# 1.4 Print the student's name and all the subjects they are studying.
"""

student = {
    "Name" : "John Doe",
    "Age" : 20,
    "Grade" : "A",
    "Subjects" : ["Math", "Physics", "Chemistry"]
}

student["Subjects"].append("Biology")
student["Age"] = 21

print(f"Name: {student['Name']}")
print(f"Subjects: {student['Subjects']}")