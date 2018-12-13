import re
from builtins import ValueError

query = """
    SELECT *
      FROM TEST_TABLE
     WHERE NAME = {name}
       AND ADDR = {addr}
       AND GNDR = {gndr}
     """
     
# print(query)     

p = re.compile('{\w+}')
f = p.findall(query)

# print(f)
# 
# print(query.replace(f[0] , repr('cyh')))

def mappingQuery(query , dic) -> str:
    searchedList = p.findall(query)
    if not len(searchedList) :
        return query
    else :
        for x in searchedList :
            key = x.replace('{','').replace('}','')
#             print("x:" , x , "dic.get(key):" , dic.get(key))
            if not dic.get(key) :
                raise ValueError("Not found exception:" , "dic has no attribute [" , key , "]")
            query = query.replace(x , repr(dic.get(key)))
    
    return query        
    
param = {'name':'cyh' , 'addr':'seoul' , 'gndr':'1'}

print(mappingQuery(query, param))

