##Decorator

def hello(func):
    def greet(*args, **kwargs):
        print("start the execution")

        sum_value = func(*args, **kwargs)
        print("Execution ended")

        return sum_value

    return greet
@hello
def sum(a,b):
    print("I am inside a number")
    return str(a+b)

a, b = (2, 3)

print("Sum of 2 numbers is: "+sum(a,b))