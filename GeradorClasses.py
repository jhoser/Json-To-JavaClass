import json
from jinja2 import Environment, FileSystemLoader

attributeList = []
arrayList = []
stringList = []

def loadJson():
    file = open("teste.json")
    fileJson = json.load(file)
    return fileJson

#def treatList(key, attributeValue, visited):
#    for attribute,attributeValue in attributeValue.pop().items():
#        if(attribute not in visited[key]):
#            visited[key][attribute] = type(attributeValue)
#            if(isinstance(attributeValue,list)):    
#                visited[attribute] = treatList(key, attributeValue,visited.copy())
#    return visited
#

def dfs(object_, keys, visited):
    if(isinstance(object_, dict)):
        for key, attributes in object_.items():
            print(attributes)
            if(key not in visited):
                visited[key] = {}
            for attribute,attributeValue in attributes.pop().items():
                print(f"attribute :{attribute} || attributeValue :{type(attributeValue)} ")
                if(attribute not in visited[key]):
                    visited[key][attribute] = type(attributeValue)
                if not isinstance(attributeValue, str):
                    visited = dfs(attributeValue, attribute, visited.copy())

        return visited

    elif(isinstance(object_, list)):
        if(keys not in visited):
            visited[keys] = {}
        for attribute,attributeValue in object_.pop().items():
            if(attribute not in visited[keys]):
                visited[keys][attribute] = type(attributeValue)
                if not isinstance(attributeValue, str):
                    visited = dfs(attributeValue, attribute, visited.copy())
        return visited

    elif(isinstance(object_, object)):
        print(keys)
        if keys not in visited:
            visited[keys] = {}
            for attribute, attributeValue in object_:
                visited[keys][attribute] = type(attributeValue)
                if not isinstance(attributeValue, str):
                    visited = dfs(attributeValue, attribute, visited.copy())
        return visited

if __name__ == '__main__' :
    dictJson = loadJson()
    #print(dictJson)
    visited = dfs(dictJson, "", {})
    #print(visited)
