import json

data = {
    "Name": "John Doe",
    "Age": 30,
    "Country": "USA",
    "city" : "New York",
    "skills": ["Python", "JavaScript", "C++"],
}
with open("learn.json", "w") as file:
    json.dump(data, file, indent=4)