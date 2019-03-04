# Source : https://www.programiz.com/python-programming/decorator
def decorate_func(func):
    def print_decorate():
        print "I have got decorated!!"
        func()
    return print_decorate

# @decorate_func
def normal_func():
    print "I am normal"

# normal_func()


pretty = decorate_func(normal_func)
pretty()