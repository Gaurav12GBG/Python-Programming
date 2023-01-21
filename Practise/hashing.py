


HT=[ [] for _ in range(10)]
print(HT)

def insert(HT,key, value):
    loc=key%10
    bucket=HT[loc]
    exist=False
    for i ,kv in enumerate(bucket):
        k,v=kv
        if(key==k):
            exist=True
            break
        if exist==True:
            bucket[i]=(key,Value)
            
        else:
            bucket.append((key ,Value))
            
def delete(HT,key):
    loc=key%10
    bucket=HT[loc]
    exist=False
    for i ,kv in enumerate(bucket):
        k,v=kv
        if(key==k):
            exist=True
            break
        if exist==True:
            del bucket[i]
            
        else:
            print("Element notfound to delete")
            
           
def search(HT,key):
    loc=key%10
    bucket=HT[loc]
    exist=False
    for i ,kv in enumerate(bucket):
        k,v=kv
        if(key==k):
            exist=True
            break
        if exist==True:
            print("Element is found")
            
        else:
            print("Element notfound ")
            
def display(HT):
    for i ,bucket in Element(HT):
        print("Bucket",i,"Elements",bucket)
        
        
print("---------Main program")
while True:
    print("1.insert")
    print("\n2.delete")
    print("\n3.search")
    print("\n4.display")
    print("\n0.exit")
    
    ch=int(input("Enter your choice:"))
    if(ch==1):
        n=int(input("Enter the how many elements you want toinsert:"))
        for i in range(n):
            key=int(input("Enter the key:"))
            value=input("Enter the value")
            insert(HT,key,value)
        print(HT)
            
        
       
        
    elif(ch==2):
        key=int(input("Enter the key:"))
        delete(HT,key)
     
        
    elif(ch==3):
        key=int(input("Enter the key:"))
        search(HT,key)
        
    elif(ch==4):
        display(HT)
        
    elif(ch==0):
        break
    else:
        print("Wrong choice")
        
        
            
            

    
            

    