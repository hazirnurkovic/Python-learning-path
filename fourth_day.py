# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Lara'
dog['color'] = 'white'
dog['breed'] = 'Syberian Samoyed'
dog['legs'] = 4
dog['age'] = 3

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary\
student = {
    'first_name': 'Lejla',
    'last_name': 'Nurkovic',
    'gender': 'female',
    'age': 26,
    'marital status': 'married',
    'skills': ['Arhitecture', 'Design', 'Arhicad', 'Photoshop'],
    'country': 'Montenegro',
    'city': 'Podgorica',
    'address': 'Stari Aerodrom'
}

# Get the length of the student dictionary
length = len(student)
print(length)

# Get the value of skills and check the data type, it should be a list
skills = student['skills']
print(skills)
print(type(skills))

# Modify the skills values by adding one or two skills
student['skills'].append('Revit')
student['skills'].append('AutoCad')
print(student['skills'])

# Get the dictionary keys as a list
list_keys = list(student.keys())
print(list_keys)

# Get the dictionary values as a list
list_values = list(student.values())
print(list_values)

# Change the dictionary to a list of tuples using items() method
student_list = student.items()
print(student_list)

# Delete one of the items in the dictionary
del student['gender']
print(student)

# Delete one of the dictionaries
del dog