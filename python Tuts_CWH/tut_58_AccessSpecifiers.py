""" 
Naming Convention in Python :
Public => simply we can write as a variable
Protected => we can write single underscore with variable name
Private => We can write double underscore with variable name

"""
class AccessSpecifier:
    var = "public"
    _var = "protected"
    __var = "private"

as1 = AccessSpecifier()
print(as1.var)
print(as1._var)
# print(as1.__var)  ---> Not accessible

