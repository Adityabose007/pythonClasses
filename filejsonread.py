import json

with open("learn.json", "r") as f:
    data = json.load(f)

    print(data)

    print(data["Name"])
    print(data["city"])
    print(data["skills"][0])