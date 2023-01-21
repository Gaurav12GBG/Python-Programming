num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second Number: "))

f = open("Addition.txt", "w") 
f.write(f"The addition of {num1} + {num2} = {num1 + num2}")
print("Result Stored successfully!")

f.close()