import csv
import matplotlib.pyplot as plt

more = 0
less = 0

with open('library_visits.csv', 'r') as file:
    reader = csv.reader(file)
    
    next(reader)  
    
for row in reader:
    visits=int(row[1])
    
if visits > 3:
    more += 1
else:
    less += 1

labels = ['More than 3 visits', '3 or fewer visits']
sizes = [more, less] 

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Library Visits Distribution")
plt.show()
