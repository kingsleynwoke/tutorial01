def new_function():
    print("function after decoration")
    
def decorating_function(decorated_function):
    def inner_function():
        print("Inner function before decuration")
        decorated_function()
    return inner_function


new_function = decorating_function(new_function)
new_function()

@decorating_function
def new_function():
    print("function after decoration")
    
new_function()

def multiply(a, b):
    print(a*b)

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def divide(a, b):
    try:
        return a*b
    except:
        return "Division by zero not possible"


def take_input(func):
    print("new1")
    def user_choice():
        print("Start1")
        choice_1, choice_2 = input("Choose two numbers a and b: ").split()
        func(int(choice_1), int(choice_2))
        print("Start2")
    print("New2")
    return user_choice


def take_input2(func):
    def user_choice(a=4, b=4):
        #print("I am going to divide", a, "and", b)
        #a, b = input("Choose two numbers a and b: ").split()
        return func(int(a), int(b))
    return user_choice


# multiply = take_input2(multiply)
# multiply()
@take_input2
def multiply(a, b):
    return a*b

@take_input2
def add(a, b):
    return a+b

@take_input2
def sub(a, b):
    return a-b

@take_input2
def divide(a, b):
    try:
        return a/b
    except:
        return "Division by zero not possible"
    
print(multiply())
print(add())
print(divide(2,3))