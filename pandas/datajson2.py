import json
from tabulate import tabulate

with open('data.json', 'r') as file:
    jsondata = json.load(file)

table=[]
count = 0
for data in jsondata:
    row=[]
    if count == 0:
        for a in data.keys():
            row.append(str(a))
        count += 1
    for b in data.values():
        row.append(str(b))
    table.append(row)

print(tabulate(table, tablefmt='grid'))
