import csv

people = [
        {'name': 'Maria', 'age': 25, 'job': 'Scientist'},
        {'name': 'Wes', 'age': 8, 'job': 'Programmer'},
        {'name': 'Greg', 'age': 48, 'job': 'Big boss'},
    ]

with open('people.csv', 'w', encoding='utf8', newline='') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in people:
        writer.writerow(user)
