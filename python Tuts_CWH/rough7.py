"""
Problem Statement :
"""
Number = int(input("Enter how many numbers you want to insert  in the list :"))
print("Enter the number that you want to store into the list :")
list = []
for i in range(0, Number):
        n = int(input())
        list.append(n)

print(f"The numbers entered by user in the list = {list}")

def even_Odd(list):
        even = []
        odd = []
        for i in list:
                if i % 2:
                      even.append(i)
                else:
                      odd.append(i)

        return even, odd

same_list = list
even, odd = even_Odd(same_list)

print(f"Even numbers from the list = {even}")
print(f"Odd numbers from the list = {odd}")


"""
Output : Enter how many numbers you want to insert  in the list :10
         Enter the number that you want to store into the list :
         12
         48
         5
         7
         0
         78
         95
         101
         958
         456
         The numbers entered by user in the list = [12, 48, 5, 7, 0, 78, 95, 101, 958, 456]
         Even numbers from the list = [5, 7, 95, 101]
         Odd numbers from the list = [12, 48, 0, 78, 958, 456]
"""