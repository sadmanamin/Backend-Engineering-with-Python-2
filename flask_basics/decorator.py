def myhome(home_function):
    def inside_func():
        print('I am inside a nested function')
        home_function()

    return inside_func

@myhome
def home():
    print('I am inside home')

# house = myhome(home)
# house()

home

