'''
LEGB
Local, Enclosing, Global, Built-in
'''

# # ## Global Scope - Assigned in the main file itself.
# # x = 'global x'

# # def test():
# #     ## Local Scope - Defined in a specific function or method
# #     # y = 'local y'

# #     ## To define a global variable in a function
# #     # global x

# #     x = 'local x'
# #     # print(y)
# #     print(x)

# # test()
# # # print(y) # NameError - Not Defined
# # print(x)

# # x = 'global x'

# def test(z):
#     x = 'local x'
#     print(z)

# test('local z')
# # print(z) # NameError



# ### Built-in Scope

# ## Viewing variables in built-in scope
# import builtins

# # print(dir(builtins))

# def my_min(): # Be careful when defining built-in functions
#     pass

# m = min([5, 1, 4, 2, 3])
# print(m)


### Enclosing Scope 
# #- Checks if there are variables in any enclosing functions

x = 'global x'

def outer():
    # x = 'outer x'

    def inner():
        # nonlocal x # nonlocal - will affect variables within the function
        # x = 'inner x'
        print(x)
    
    inner()
    print(x)

outer()
print(x)