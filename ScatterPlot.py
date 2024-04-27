import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('C:\\Users\\HP\\Documents\\PT6\\dataset - 2020-09-24.csv')

print(df.head(5))
print(df.info())
print(df.describe())
missing_values = df.isnull().sum() 
print(missing_values)

#Finding and Counting Duplicates
duplicates = df.duplicated().sum()
print("Number of duplicates:", duplicates)

plt.scatter(df['Wins'], df['Losses'])
plt.title('Wins vs Losses Scatter Plot')
plt.xlabel('Wins')
plt.ylabel('Losses')
plt.grid(True)
plt.show()  