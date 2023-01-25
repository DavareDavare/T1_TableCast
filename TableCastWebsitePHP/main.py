import json

# Load the JSON file into a variable
with open('data.json') as json_file:
    data = json.load(json_file)

# Access individual variables from the JSON file
print(data['Helligkeit'])
print(data['Geschwindigkeit'])
print(data['Text'])