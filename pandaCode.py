import pandas as pd

mydata = {

    'Name' : ["Alice", "Bob", "Charlie"],
    'Age'  : [25, 26, 27],
    'Salary' : [40000, 60000 , 77770]
}

df = pd.DataFrame(mydata)

print(df)
print(df["Name"])

#Task 1: student marks analysis
#Goal:
#ananlyze the marks of students over multiple subjects.
#[85, 78, 92, 88],
#[76, 81, 79, 75],
#[90, 94, 88, 92],
#[65, 70, 72, 68],
#[88, 85, 91, 89]

#Task 2: Tracker (weekly)
#Goal:
#Track personal expenses under 3 categories: Food, Travel, Others


#expenses = np.array([
#    [120, 50, 30],
#    [100, 60, 40],
#    [130, 45, 25],
#    [110, 70, 20],
#    [115, 65, 35],
#    [140, 55, 45],
#    [125, 60, 30]
#])
