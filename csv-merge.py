import pandas as pd

csv1 = pd.read_csv("book2.csv")
csv2 = pd.read_csv("book1.csv")

#Using merge function by setting how='inner'
output1 = pd.merge(csv1, csv2, 
                   on='name', 
                   how='left')

# Export merged pandas DataFrame s
output1.to_csv('data_merge.csv', index = False)  

#Displaying result
print(output1)


