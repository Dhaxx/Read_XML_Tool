import xml.etree.ElementTree as ET

tree = ET.parse('work.xml')
root = tree.getroot()
for row in root.iter('ROW'): # <--- vai procurar somente por ROW
    print("CODIGO_BAI: " + row.attrib['Column2'] + " | " + "EMPRESA_BAI" + row.attrib['Column3'] + " | " + "DESCRICAO_BAI: " + row.attrib['Column4'] + " | " + "CODIGO_TCE_BAI: " + row.attrib['Column5'] + " | " + "CHK_DESM_BAI: " + row.attrib['Column6']) 
    print("\n")