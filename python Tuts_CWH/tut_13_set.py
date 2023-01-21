
# Set
#1: { } Representation
#2: ordered o/p
#3: Duplicate value are not allowed
#4:Unique value
#5:We can store any type of data

# IMPLEMENTATION :
s= {1,2,3,4,5,6,7,8,2,4,3}
print("This is a set:",s)
#===========================================================================================================
s1= {1,2,3,4,6,2,3,4,8,8,3}
print("This is a set:",s1)

ls= ["Gaurav","Raghav","Krutika","Swaraj","Pratiksha","Vaishnavi","Gaurav"]
print(set(ls))   # conversion of list into set

tup= (5,4,8,1,6,3,3,2,0)
print(set(tup))  # conversion of tuple into set
print(type(tup))

print(type(s1))
print(len(s1))

s2= set()
print(s2)

s2.add(20)
print(s2)

tup1= (44,55,22,11)
s2.add(tup1)
print(s2)

'''ls1= [12,13,14,15]
s2.add(ls1)
print(s2)'''


