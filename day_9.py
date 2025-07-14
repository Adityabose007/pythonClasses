import csv

with open("names.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age","Country"])
    writer.writerow(["Aditya", 21,"INDIA"])
    writer.writerow(["John", 25,"USA"])
    
    