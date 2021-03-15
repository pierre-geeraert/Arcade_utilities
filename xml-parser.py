import xml.etree.ElementTree as ET
Files_read = ET.parse('XML/ColecoVision.xml')
XML_object = Files_read.getroot()
for x in XML_object.findall('game'):
    game_name =x.find('description').text
    print(game_name)