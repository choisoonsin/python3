# -*- coding:utf-8 -*-
from xml.etree.ElementTree import Element , SubElement , dump

resource = Element("resource" , {"ADAPTER_NAME":"STBK" , "DESCRIPTION":"설명"})

interface = Element("interface" , {"ID":"KIBN_COMMON" , "SR_TYPE":"C"})

field = Element("field" , {"ID":"LENGTH" , "NAME":"길이" , "TYPE":"9" , "LENGTH":"4"})
interface.append(field)

resource.append(interface)

interface = Element("interface" , {"ID":"STBK_COMMON" , "SR_TYPE":"C"})

resource.append(interface)

dummy = Element("dummy")
dummy.text = "dummy!!"
resource.insert(2 , dummy)

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
            
indent(resource) 
dump(resource)           