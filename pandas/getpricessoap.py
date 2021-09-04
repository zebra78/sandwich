import xml.etree.ElementTree as ET
import pandas as pd
import json


namespaces = {
    'soap': 'http://www.w3.org/2003/05/soap-envelope/',
    'm': 'https://www.w3schools.com/prices',
}

tree = ET.parse('getpricesoap.xml')
root = tree.getroot()

names = root.findall(
    './soap:Body',
    namespaces,
)

for child in root:
    if len(child):
        print("->HasSubElem", end='')
    else:
        print("->", child.text, end='')

    for child1 in child:
        if len(child1):
            print("->HasSubElem", end='')
        else:
            print("->", child1.text, end='')
        for child2 in child1:
            if len(child2):
                print("->HasSubElem", end='')
            else:
                print("->", child2.text, end='')
            print()
