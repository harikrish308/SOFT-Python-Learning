# 30 Days of Python: Day 8 - Dictionaries Exercise Solutions

# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, and age to the dog dictionary
dog = {
    'name': 'Buddy',
    'color': 'Golden',
    'breed': 'Golden Retriever',
    'legs': 4,
    'age': 3
}

# 3. Create a student dictionary and add keys
student = {
    'first_name': 'Hari',
    'last_name': 'Krishnan',
    'gender': 'Male',
    'age': 18,
    'marital_status': 'Single',
    'skills': ['Python', 'HTML', 'JavaScript'],
    'country': 'India',
    'city': 'Kochi',
    'address': {'street': 'MG Road', 'zipcode': '682016'}
}

# 4. Get the length of the student dictionary
print("4. Length of student dictionary:", len(student))

# 5. Get the value of skills and check the data type (should be a list)
print("5. Skills value:", student.get('skills'))
print("   Data type of skills:", type(student['skills']))

# 6. Modify the skills values by adding one or two skills
student['skills'].append('React')
student['skills'].append('Node')
print("6. Modified skills:", student['skills'])

# 7. Get the dictionary keys as a list
keys_list = list(student.keys())
print("7. Keys list:", keys_list)

# 8. Get the dictionary values as a list
values_list = list(student.values())
print("8. Values list:", values_list)

# 9. Change the dictionary to a list of tuples using the items() method
student_tuples = list(student.items())
print("9. List of tuples:", student_tuples)

# 10. Delete one of the items in the dictionary
student.pop('marital_status')
print("10. Student dictionary after deleting 'marital_status':", student)

# 11. Delete one of the dictionaries
del dog
print("11. 'dog' dictionary has been deleted.")