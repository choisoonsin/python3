# -*- coding:utf-8 -*-
from xml.etree.ElementTree import Element, SubElement , dump, indent

root_el = Element("FRUITS" , {"DESCRIPTION":"FRUIT SCHEME"})
fruit_el = Element("FRUIT" , {"ID":"FR0001" , "KO_NAME":"바나나" , "EN_NAME":"BANANA"})
root_el.append(fruit_el)

fruit_sub_el = Element("FIELD" , {"당도":"4"})
fruit_el.append(fruit_sub_el)
fruit_sub_el = Element("FIELD" , {"가격":"4000"})
fruit_el.append(fruit_sub_el)

interface = Element("FRUIT" , {"ID":"FR0002" , "KO_NAME":"사과" , "EN_NAME":"APPLE"})

root_el.append(interface)

dummy = Element("dummy")
root_el.insert(4 , dummy)
SubElement(dummy, "test", {"attr1":"test", "attr2":"5000", "attr3":"True"})

indent(root_el) 
dump(root_el)           