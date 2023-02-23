# DECORATOR: decorators wrap a function, modifying its behavior.

def say_hi(name):
    return f"Hello {name}"

say_hi("bora")

def say_hello(func):
    return func("Bora")

say_hello(say_hi)  # *** We gave a function as an argument to function.


# Inner Functions: define functions inside other functions
def meeting():
    print("Hi guys!, I am host")
    def hi_from_john():
        print("Hello")
    def hi_from_erik():
        print("Hey Hey")

    hi_from_john()
    hi_from_erik()

meeting()


# Returning Functions From Functions
def meeting():
    print("Hi guys!, I am host")
    def hi_from_john():
        print("Hello")
    def hi_from_erik():
        print("Hey Hey")

    hi_from_john()
    hi_from_erik()

    return hi_from_john, hi_from_erik

hi_from_john , hi_from_erik = meeting()
hi_from_john()


# Basic Decorator Templates
import functools
def my_decorator(func):
    @functools.wraps(func)
    def wrapper():  # Here, the actions to be taken regarding the function that the decorator will host are defined.
        print("Do something before the function call.")
        func()
        print("Do something after the funciton call.")
    return wrapper

@my_decorator
def say_hi():
    print("Hello")

say_hi()
# Do something before the function call.
# Hello
# Do something after the funciton call.


say_hi.__name__  # : Function's name turned into wrapper name, in order to fix this, we use functools.wrap


# Decorating Functions With Arguments
import functools
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Do something before the function call.")
        func(*args, **kwargs)
        print("Do something after the function call.")
    return wrapper

@my_decorator
def say_hi(name):
    print(f"Hello {name}")

say_hi("Bora")  # wrapper() takes 0 positional arguments but 1 was given
# we gave an argument to function but wrapper does not aware of this.

# We can pass variable number of arguments to a function using special symbols
#       *args (Non-Keyword Arguments)
#       **kwargs (Keyword Arguments), (Dictionary)
#       We can create a general purpose decorator with this symbols.


########################################################################
#                           PRACTICES
########################################################################

# Practice-1 Party Boy Decorator
import functools
def party_boy(func):
    @functools.wraps(func)
    def wrapper(name):
        print("Welcome to party!")
        func(name)
        print("Goodbye!")
    return wrapper

@party_boy
def bora(with_who):
    print(f"I am eating, drinking, dancing with my friends {with_who}!")

bora("eren")


# Practice-2 Timing Functions
import time
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def sum_of_even_numbers(numbers):
    even_sum = 0
    for number in range(numbers):
        if number % 2 == 0:
            even_sum += number
    return even_sum

sum_of_even_numbers(100*100)



#################
# EXTRA
#################
########################################################################
# Applying Multiple Decorators to a Single Function
########################################################################

def split_text(func):
    def wrapper_split(*args):
        txt = func(*args)
        splited_text = txt.split()
        return splited_text
    return wrapper_split

def uppercase_text(func):
    def wrapper_upper(*args):
        txt = func(*args)
        uppered_text = txt.upper()
        return uppered_text
    return wrapper_upper

@split_text
@uppercase_text
def make_text(text):
    return text

make_text("Bora Tutumluer")




