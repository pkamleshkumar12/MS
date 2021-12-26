import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": [
        "engineer",
        "programmer"
    ]
}

person_json = json.dumps(person, indent=4, sort_keys=True)

print(person_json)
# dumps and dump are 2 separate methods

with open('person.json', 'w') as file:
    json.dump(person, file)

# deserialization or decoding
person_des = json.loads(person_json)
print(person_des)

with open('person.json', 'r') as file:
    person_f = json.load(file)
    print(person_f)
