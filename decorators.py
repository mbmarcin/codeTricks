import datetime

#====================================================================================
def time_decorator(func):
    def inner1():
        print(f"Start time is : {datetime.datetime.now()}")
        func()

        print(f"End time is : {datetime.datetime.now()}")

    return inner1


@time_decorator
def test_decorator_simple():
    print(f"Time in test : {datetime.datetime.now()}")
#=========================================================================================

class decorator_with_arguments(object):

    def __init__(self, arg1, arg2, arg3):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print("Inside __call__()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", self.arg1, self.arg2, self.arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f

@decorator_with_arguments("Donald", "Le", "1990")
def test_decorator_with_arguments():
    print("Testing decorator with arguments")

# def ordinary():
#     print("I am an ordinary function.")
    
    
def decorate(function):
    def inner_function():
        print("I was decorated!")
        function()
    return inner_function

@decorate
def ordinary():
    print("I am an ordinary function.")
    
ordinary()


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
#
# @my_decorator
# def say_whee():
#     print("Whee!")
#
# #say_whee = my_decorator(say_whee)
#
# say_whee()


# -------------------------------------------------------------------------------------


# from datetime import datetime
#
#
# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 21:
#             func()
#         else:
#             print('psst!')  # Hush, the neighbors are asleep
#
#     return wrapper
#
#
# @not_during_the_night
# def say_whee():
#     print("Whee!")
#
# say_whee()

# -----------------------------------------------------------------------------------

# def do_twice(func):
#     def wrapper_do_twice():
#         func()
#         func()
#
#     return wrapper_do_twice
#
# @do_twice
# def say_whee():
#     print("Whee!")
#
# say_whee()

# Decorating Functions With Arguments----------------------------------------------------

# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper_do_twice


# @do_twice
# def greet(name):
#     print(f"Hello {name}")
#
# @do_twice
# def say_whee():
#     print("Whee!")
#
# say_whee()
# greet('mm')


# Returning Values From Decorated Functions

# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#
#     return wrapper_do_twice
#
#
# @do_twice
# def return_greeting(name):
#     print("Creating greeting")
#     return f"Hi {name}"
#
#
# print(return_greeting('adam'))

#example--------------------------------------------
# import functools
#
# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(100)











