"""
Looping and Lists
3.1 Create a list of names and use a for loop to print a personalized greeting message for each
name. For example, "Hello, John!" for the name 'John'.
3.2 Use a while loop to find the first name in the list that starts with a vowel.
"""

names = ["John", "Jane", "Ack", "Eill", "James", "Jenny", "Vesse", "Jasmine", "Jared", "Jocelyn"]

for name in names:
    print(f"Hello, {name}")

while names:
    name = names.pop(0)
    if name[0].lower() in "aeiou":
        print(f"First name that starts with a vowel: {name}")
    else:
        print(f"Name that does not start with a vowel: {name}")