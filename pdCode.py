import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Emily', 'Bob', 'arkit'],
    'Age': [25, np.nan,40,np.nan, 25, 35, 45],
    'salary':[3000,6000,np.nan,80000,40000,50000,10000]
    
}


df = pd.DataFrame(data)

salary = df["salary"].dropna()
plt.boxplot(salary)

plt.title("Outlier detection")
plt.ylabel("salary")
plt.show()


#df = pd.DataFrame(data)
#print(df.duplicated())
#df_clenaed = df.drop_duplicates()
#print(df_clenaed)



#duplicate data



#print(df.isnull())
#print(df.isnull().sum())


#ffill = df.fillna(method='ffill')
#bfill = df.fillna(method = "bfill")

#print(ffill)
#print(bfill)

#df_filled = df.fillna(0)
#print(df_filled)


#df_filled = df["salary"].fillna(df["Age"].mean())
#print(df_filled)


#df_cleaned = df.dropna()#Removes rows with null values
#print(df_cleaned)






# d:\pythonClasses\pdCode.py
#df = pd.DataFrame(data)
#print
#df.to_csv("learnpandas.csv" , index = False)

#df = pd.read_csv("business-fianancial-data-march-2025-quarter-csv.csv")
#print(df)
#print(df.head())
#print(df.tail())


#index = ['user1', 'user2', 'user3', 'user4','user5','user6','user7']
#df = pd.DataFrame(data)
#print(df)


#print(df.loc['user3'])
#print(df.loc[2])


#df["experience"]=[2,3,4,5,6]
#df.loc[1, 'salary'] = 65000
#print(df[:2])
#print(df.loc[1:3, ['Name' , 'salary']])

#print(df)

#print(df.loc[1:3, ['Name', 'salary']])
#df.loc[1, 'Salary'] = 65000 #update john's salary
#print(df)

#print(df)
#print(df["Name"])