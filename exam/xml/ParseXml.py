# -*- coding:utf-8 -*-
from xml.etree.ElementTree import parse , dump
from builtins import type

xml = parse("KFTC_REG.xml")
# print(type(xml))
# dump(xml)

rootNode = xml.getroot()
print(rootNode.get("ADAPTER_NAME"))

print("keys" , rootNode.keys())

for x in rootNode.keys():
    print(x , "=" , rootNode.get(x))

# print(rootNode)

# interfaceList = rootNode.findall("interface")
# print("____test____")
# print(list(rootNode.getiterator("interface")))

xx = 100
xxx = 500

def getInterfaceElement(Node , id):
    interfaceList = Node.getiterator("interface")
    for x in interfaceList:
        if x.get("ID") == id :
#             print(x.get("ID"))
            return x
            
    print("could not find this id[" , id , "]")
    return None

def getChildElementById(rootNode , childTag , childId):
    try:
        xx = 10
        xxx = 5
        interfaceList = rootNode.getiterator(childTag)
    except AttributeError as f:
        print("Could not find this tag:" , childTag)
        print(f)
        return None
            
    for x in interfaceList:
        print(xx)
        print(xxx)
        if x.get("ID") == childId :
#             print(x.get("ID"))
            return x
            
    print("could not find this childId[" , childId , "]")
    return None

def getChildElements(Node):
    returnList = []
    for x in Node.getiterator("field"):
        returnList.append(x)
        
    return returnList
    

# dump(getInterfaceElement(rootNode , "TKFSCMS410"))
 
# dump(getChildElementById(rootNode , "interface" , "TKFSCMS400"))

interface = getChildElementById(rootNode , "interface" , "TKFSCMS400")

class DataVo :
    def __init__(self , id , name , type , length):
        self.id = id
        self.name = name
        self.type = type
        self.length = length
    
    def toString(self):
        return "[id=" + str(self.id) + ", name=" + str(self.name) + ", type=" + str(self.type) + ", length=" + str(self.length) + "]"
        
d = DataVo("Tran_CD" , "거래구분코드" , 9 , 6)

print(d.toString()) 

# print(getChildElements(interface))

def getDataVoList(InterfaceNode):
    dataVoList = []
    ''' x is field element '''
    for x in getChildElements(interface):
        _id = x.get("ID")
        _name = x.get("NAME")
        _type = x.get("TYPE")
        _length = x.get("LENGTH")
        dataVoList.append(DataVo(_id , _name , _type , _length))
        
    return dataVoList

print(getDataVoList(interface))
    
for x in getDataVoList(interface):
    if x.id == None : continue
    
    print(x.toString())






