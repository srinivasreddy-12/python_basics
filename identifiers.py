#IDENTIFIERS
'''
Rules for identifiers
1)Allowed characters =>alphabets and digits and underscore
2)identifiers should never start with digits
3)case sensitive
4)no length limit
5)cany't use keyword as identifiers  
'''
abc123 = 100
_123 = 200
print(abc123 + _123)

import keyword
print(keyword.kwlist)#printing key words which are not used as identifiers or variables
print("There are these many ",len(keyword.kwlist)," key words")#length of key words

Abc123 = 300

print(id(abc123))#case sensitive
print(id(Abc123))

a = 10
b = 10
print(id(a))#Both will get same address
print(id(b))