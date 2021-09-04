import xml.etree.ElementTree as ET
import pandas as pd
import json

tree = ET.parse('country.xml')
root = tree.getroot()

for child in root:
    if len(child):
        print("HasSubElem", end='')
    else:
        print(child.text, end='')

    for child1 in child:
        if len(child1):
            print("HasSubElem", end='')
        else:
            print(child1.text, end='')
        for child2 in child1:
            if len(child2):
                print("HasSubElem", end='')
            else:
                print(child2.text, end='')
    print()
