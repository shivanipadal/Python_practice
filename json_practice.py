import json 

#Convert from JSON to Python:
x = '{"name": "JSON", "age": 30, "city": "New york"}'
y = json.loads(x)
print(y['age'])

#Convert from Python to JSON
x = {
    'name': 'John',
    'age': 30,
    'city': 'New york',
    }

#convert into json 
y = json.dumps(x)
print(y)


####################################################

# Convert a Python object containing all the legal data types:

# import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x)) #will print all in one line and it is not easy to read with no indentations and line breaks 

print(json.dumps(x, indent=4)) #Easy to read by prviding the indent parameter value

