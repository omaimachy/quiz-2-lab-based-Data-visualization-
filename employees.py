import matplotlib.pyplot as plt
import csv
import pandas as pd

data = pd.read_csv('employees.csv')
high_salary = data[data['salary'] > 50000]
high_salary = high_salary.sort_values(by="name")

print(high_salary)
count = high_salary['department'].value_counts()
print(count)
count.plot(kind='bar', color='green')

plt.xlabel('Department')
plt.ylabel('Number of high-salary Employees')
plt.title('Employee Distribution by Department')
plt.tight_layout()
plt.show()

