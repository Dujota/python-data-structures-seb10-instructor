favorite_animal = 'dog'

student = {
    'name': 'Maria',
    'favorite_integer': 5,
    favorite_animal: 'llama' # notice the lack of quotes around favorite_animal
}

print(student)
# prints: {'name': 'Maria', 'favorite_integer': 5, 'dog': 'llama'}
# note the 'dog' key - the value of the favorite_animal variable is used


# ACCESSING VALUES FROM DICT

# cannot access a key that doesnt exist in the obj
# favorite_food = student['favorite_food']

# Use the dict.get(key) method
random_key = 'dsadsadadsasfag'

result = student.get(random_key)

if result:
  print('exists')
else:
  print('does not exist')

print(result)

if 'course' in student:
    print(f"{student['name']} is enrolled in {student['course']}")
else:
    print(f"{student['name']} is not enrolled in a course")
    # prints: Maria is not enrolled in a course


# HOW TO UPDATE OBJECTS

# Add a new key-value pair
student['name'] = 'Mariana'
print(student['name'])

student['name'] = 'TEST'
print(student['name'])

del student['dog']
# verify that the item was deleted
print('dog' in student)

print(len(student))

print(len({}))
print('=====================')
# Looping through a dictionary

# BAAAAAAAD WAAAAY ... dont be a js head
for key in student:
    print(f"{key} is {student[key]}")


print('=====================')
print(student.items())
# GOOD WAY - use the items() method
for key, val in student.items():
    print(f"{key} is {val}")
    # prints:
    # name is Maria
    # favorite_integer is 5
    # age is 25
print('=====================')