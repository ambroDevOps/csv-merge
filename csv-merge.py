import pandas as pd

csv1 = pd.read_csv("book2.csv")
#csv1.head()
csv2 = pd.read_csv("book1.csv")
#csv2.head()

# using merge function by setting how='inner'
output1 = pd.merge(csv1, csv2, 
                   on='name', 
                   how='left')
  
output1.to_csv('data_merge.csv', index = False)  # Export merged pandas DataFrame

# displaying result
print(output1)


