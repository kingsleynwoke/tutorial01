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

