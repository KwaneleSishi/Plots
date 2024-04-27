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

plt.figure(figsize=(10,8))
plt.bar(df['Name'],df['Wins'])
plt.xlabel('Player Name')
plt.ylabel('Wins')
plt.title('No.of Wins by Player')
plt.xticks(rotation=90)
plt.show()