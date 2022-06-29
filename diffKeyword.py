#non keyword argument
def add(*num):
    sum = 0

    for i in num:
        sum += i
    print("sum : ", sum)

add(10, 20)
add(10, 20, 30)    

#keyword argument
def my_fun(**arg):
    for i, j in arg.items():
        print(i, j)

my_fun(name = "xyz", lastname = "pqr")
