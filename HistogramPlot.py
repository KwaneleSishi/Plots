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
for club in df['Club'].unique():
    plt.hist(df[df['Club'] == club]['Wins'], bins=20, alpha=0.5, label=club)

plt.xlabel('Wins')
plt.ylabel('Frequency')
plt.title('Distribution of Wins by Club')
plt.legend()
plt.grid(True)
plt.show()
