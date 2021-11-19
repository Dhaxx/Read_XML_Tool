import xml.etree.ElementTree as ET

tree = ET.parse('File.XML') # Here go your XML file name
root = tree.getroot()

filtro = '*'

for row in root.iter(filtro): 
    print(row.tag, row.attrib)