import json

# Assuming you have a JSON file named person.json
with open('person.json', 'r') as f:
    person_dict = json.load(f)

# Accessing the parsed data
print(person_dict["name"])  # Output might be: John Doe, depending on your JSON file's content
print(person_dict["age"])   # Similarly, output depends on your file's content