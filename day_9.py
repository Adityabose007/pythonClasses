import csv

'''data = [
    ["Name", "Age", "Country"],
    ["Aditya", 21, "INDIA"],
    ["John", 25, "USA"],
    ["Alice", 30, "UK"],
    ["Bob", 35, "Australia"],
    ["Charlie", 28, "Canada"],
    ["Diana", 22, "Germany"],
]'''

'''dataDict = [
    {"Name": "Aditya", "Age": 21, "Country": "INDIA",},
    {"Name": "John", "Age": 25, "Country": "USA"},
    {"Name": "Alice", "Age": 30, "Country": "UK"},
    {"Name": "Bob", "Age": 35, "Country": "Australia"},
    {"Name": "Charlie", "Age": 28, "Country": "Canada"},
    {"Name": "Diana", "Age": 22, "Country": "Germany"},
]

with open("names.csv", "w", newline="") as file:

    #writer = csv.writer(file)
    fieldnames = ["Name", "Age", "Country"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dataDict)

file.close()'''



'''writer.writerow(["Name", "Age","Country"])
    writer.writerow(["Aditya", 21,"INDIA"])
    writer.writerow(["John", 25,"USA"])'''
    


    