
#dictionary ;
#1. Representation  { }
#2. written in Key:Value pair
#3. Syntax :  z = {key1:"Value1",Key2:"Value2"}

#Implementation :

std= {1:"mango",2:"Orange",3:"Banana",4:"Fruit"}

keys= ("name","sal","edu")
values=0

# type():
print(type(std))

# clear():
std.clear()
print(std)

# copy():
copied_data= std.copy()  # This is different variable of dict
print(copied_data)

# fromkeys():
newdata= dict.fromkeys(keys,values)   # This is different variable of dict
print(newdata)

#get(): It returns the value of specified keys
fruits = {11:"pinapple",22:"santra",33:"Grapes"}
store_value= fruits.get(33)
print(store_value)

#items():
new= fruits.items()
print(new)

#keys():
print(fruits.keys())

#values():
print(fruits.values())

#pop():
fruits.pop(22)
print(fruits)

#popitem:
fruits.popitem()
print(fruits)

#setdefault():
x= fruits.setdefault(11,22)
print(x)

#update():
fruits.update({44:"vaishnavi"})
print(fruits)











