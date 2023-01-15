import zipfile
import xml.etree.ElementTree as ET
import os
import pandas as pd


doc = zipfile.ZipFile('./test.docx').read('word/document.xml')
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
root = ET.fromstring(doc)

# print whole document
# print(ET.tostring(root, encoding='utf8').decode('utf8'))

t_nodes = root.findall(
    './/w:r[@w:rsidRPr]/w:t', ns)

descriptions_arr = []
start_including = False
stop_including = False
for node in t_nodes:
    if node.text == "Knowledge":
        stop_including = True
    if start_including and not stop_including:
        descriptions_arr.append(node.text)
        print(node.text, node.attrib)
        print("===========================================")
    if node.text == "Level 6":
        start_including = True

print(descriptions_arr)
