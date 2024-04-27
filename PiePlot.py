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


plt.figure(figsize=(10, 8))
club_wins = df.groupby('Club')['Wins'].sum()
plt.pie(club_wins, labels=club_wins.index, autopct='%1.1f%%', startangle=140)
plt.title('Wins Distribution by Club')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
