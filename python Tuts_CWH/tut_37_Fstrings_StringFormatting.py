# Fstrings and String Formatting :

# ways of writing string formatting
# option 1
me = "Gaurav"
person = 1
msg = "This is farmhouse of %s %s"%(me, person)
print(msg)

# option 2
name = "Gaurav"
reply = "fine"
ask_msg = "Hello {}, How are you ? I am {}"
x = ask_msg.format(name, reply)
print(x)

# best option : Increases Redeability
salary = 15000
ammount = 2000
reason = "buying some books"

a = f"Hii !, My salary is {salary} and i want {ammount} for {reason}."
print(a)

name = "gauravsxfsfd"
print(f"my name is {name}")

