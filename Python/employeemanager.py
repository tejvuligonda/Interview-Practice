'''
Given a list of manager and employee information represented in hashMap entries {AAA->BBB,CCC,EEE},{CCC->DDD}. 
Print company structure tree with proper indentations.BBB, CCC and EEE directly reports to AAA, so they have one white space before "-", DDD reports to CCC, it has two whitespace before "-". The input is map<String,List<String>>

Example input:
{AAA->BBB,CCC,EEE},{CCC->DDD}
Example output:
-AAA
 -BBB
 -CCC
  -DDD
 -EEE

Link: https://www.careercup.com/question?id=5754527530614784
'''

# Approach 1:
## 1. Create an N-ary tree out of the map and input things from left to right UPDATE: it is a graph
## 2. Output everything from right to left starting at the bottom
# Approach 2:
## 1. Find root
## 2. Put it in a list and input the children next to the parents
## 3. Iterate and output
# Approach 3:
## 1. Find all leaf nodes (lowest children)
## 2. Input into list with leaf nodes first
## 3. Iterate backwards and output
## HOW TO STORE SPACES?? tuple: (name, numSpaces)


# Assumptions:
# One employee only has one manager

from sets import Set


def takeInput(companyStructure):
    people = []
    structure = {}
    allchildren = sum(companyStructure.values(), []) # flattens list
    root = list((set(companyStructure.keys()) - set(allchildren)))[0]
    people.append(root)
    structure[root] = 0
    for k in companyStructure.keys():
        for e in companyStructure[k]:
            if root == k:
                people.append(companyStructure[k])
            else:
                #find the index of k and append e after that index
                people.insert(people.index(k)+1,e)
            structure[e] = structure[k] + 1
    printAllEmployees(people,structure) 

def printAllEmployees(people,structure):
    for p in people:
        printEmployee(p,structure[p])


def printEmployee(name,numSpaces):
    result = ""
    for i in range(numSpaces):
        result += " "
    result += "-" + str(name)
    print result

if __name__ == "__main__":
    test1 = {'AAA': ['BBB','CCC','EEE'], 'CCC': ['DDD']}
    takeInput(test1)
    test2 = {'AAA':['BBB'],'BBB':['CCC','DDD']}
    takeInput(test2) 
