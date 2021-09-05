import xml.etree.ElementTree as ET
import pandas as pd
import json
from tabulate import tabulate

tree = ET.parse('country.xml')
root = tree.getroot()

table =[]

for child in root:
    row = []
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
        row.append(child.attrib.get("name"))
    else:
        row.append(child.text)
    for child1 in child:
        if len(child1):
            row.append(child1.attrib.get("name"))
        else:
            row.append(child1.text)
        for child2 in child1:
            if len(child2):
                row.append(child2.attrib.get("name"))
            else:
                row.append(child2.text)
    table.append(row)

print(tabulate(table, tablefmt='grid'))