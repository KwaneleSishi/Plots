import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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
plt.boxplot([df[df['Club'] == club]['Wins'] for club in df['Club'].unique()], labels=df['Club'].unique())
plt.xlabel('Club')
plt.ylabel('Wins')
plt.title('Box Plot of Wins by Club')
plt.grid(True)
plt.show()
