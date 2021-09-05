import xml.etree.ElementTree as ET
import pandas as pd
import json
from tabulate import tabulate

namespaces = {
    'soap': 'http://www.w3.org/2003/05/soap-envelope/',
    'm': 'https://www.w3schools.com/prices',
}

tree = ET.parse('getpricesoap.xml')
root = tree.getroot()

names = root.findall(
    './soap:Body',
    namespaces
)

table=[]
for child in root:
    row=[]
    row.append(child.tag)
    for child1 in child:
        row.append(child1.tag)
        for child2 in child1:
            row.append(child2.tag)
    break
table.append(row)

for child in root:
    row = []
    if len(child):
        row.append("HasSubElem")
    else:
        row.append(child.text)
    for child1 in child:
        if len(child1):
            row.append("HasSubElem")
        else:
            row.append(child1.text)
        for child2 in child1:
            if len(child2):
                row.append("HasSubElem")
            else:
                row.append(child2.text)
        table.append(row)

print(tabulate(table, tablefmt='grid'))