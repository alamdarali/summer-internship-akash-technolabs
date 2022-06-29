#No argument , No return statment
def my_function():
    print("hello world")

my_function()

# argument , return statment
def My_Function(name):
    return name

name = My_Function("xyz")
print(name)

#argument , No return statment
def My_function(name):
    print("my name is ", name)

My_function("xyz")

#No argument , return statment
def my_Function():
    name = "xyz"
    #age = 39
    #BOY = 1983
    return name#, age, BOY

detail = my_Function()
print(detail)

