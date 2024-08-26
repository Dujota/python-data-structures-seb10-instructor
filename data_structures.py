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

# LISTS
colors = ['red', 'blue', 'green']

first = colors[0]
print(first)  # prints: red
last = colors[len(colors) - 1]
last = colors[-1]

colors[-1] = "purple"
print(colors[-1])  # prints: purple

# ADDING TO LISTS
# arr.push() in js --> arr.append()
colors.append('yellow')

# Append multiple items to a list
colors.extend(['black', 'white'])

colors.insert(1, 'teal')
print(colors)

# REMOVING FROM LISTS
# arr.pop() in js --> arr.pop(index)

blue = colors.pop(2)
print(colors)
print(blue)

colors[3] = 'black'
# remove by value
colors.remove('black')
print(colors)

# clean an array of its items
colors.clear()

#looping through a list
arr = ['red', 'green', 'blue']

for item in arr:
   print(item)

# 0:red 1:green 2:blue
#[(0,val), (1,val), (2,val)]
for index, item in enumerate(arr):
    print(index, item)

# TUPLES - basically a list, that cannot be changed
hello_tuple = ('Hello')
# this will not create a tuple
print(type(hello_tuple))
# prints: <class 'str'>

hello_tuple = ('Hello',)
# or just the following (remember parenthesis are not required)
hello_tuple = 'Hello',
print(type(hello_tuple))
# prints: <class 'tuple'>

colors_tuple = ('red', 'green', 'blue')
print(colors_tuple[1])
# prints: green
print(colors_tuple.index('blue'))
print('=====================')


for color in colors_tuple:
   print(color)
print('=====================')
# 0:red 1:green 2:blue
#[(0,val), (1,val), (2,val)]
for index, item in enumerate(colors_tuple):
    print(index, item)


r,g,b = colors_tuple
print('=====================')
print(r)
print(g)
print(b)