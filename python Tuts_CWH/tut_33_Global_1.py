
# Variable Scope : Global and Local Variables, Global keywords

"""
1. Local Variable :- A variable that is declared inside a function OR loop is called as local variable.
                   - It is accessible from the point where it is defined until the end of the function.
                   - Local variables cannot be accessed outside the function.
                   - The parameter names in the function , they behave like a local variable.
                   - Example shown in the following program.

2. Global Variable:- On the other hand, a global variable is easier to understand; it is not declared inside
                     a function and can be accessed anywhere within a program.
                   - It can also be defined as a variable defined in the main body of the program.
                   - Any function or loop can access it.
                   - Its scope is anywhere within the program.
                   - Example shown in the following program.

3. Global Keyword :- If we want to modify the global variable inside the function.
                   - For this purpose we used the global keyword.
                   - In python, the global keyword allows us to modify the global variable.
                   - It is used to create a global variable and make changes to the variable in the local scope.
                   - Example shown in the following program.

Rules of global keyword :- 1] If we assigned a value to a variable within the function body, it would be local
                              unless explicitly declared as global.
                           2] Those variable that are referenced only inside a function are implicitly global.
                           3] There is no need to use the global keyword outside a function.

 If we have a nested function how does the scope change ?
                   - When we define a function , it becomes a nested function.
                   - We already know ho to accessed the global variable from a function by using a global keyword.
                   - when we declared a local variable in a function its scope is restricted to that function alone.
                   - This is because each function and sub function stores its variable in its separate workspace.
                   - A nested function also has its own workspace but it can be accessed to the workspaces of all
                     functions in which it is nested.
                   - A variable whose value is assigned by the primary function can be read or overwritten by a
                     function nested at any level within the primary.
"""

"""
Local Variable and Global Variable :
"""
#
# l = 10   # Global
#
# def variable_values( n ):
#       l = 5       # local
#       print(l)
#       print(n)
#
# variable_values("RAM")

"""
Global Keyword:
"""
# Eg 2

# x = 15
# def change ():
#       global x
#       x = x + 5
#       print("Value of x inside the function:", x)
#
# change()
# print("Value if x outside the function:", x)

# Eg 3

def add():
      x = 15

      def change():
            global x
            x = 20
      print("Before making change:", x)
      print("Making change")
      change()
      print("After making change:", x)

add()
print("Value of x", x)

