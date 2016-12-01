# Errors and exceptions will *definitely* occur in your code. Be prepared!

# Python uses the "try" and "catch" keywords to capture possible errors in code.

try:
    impossible = 1/0
except ZeroDivisionError:
    print("Can't divide by zero.")

# There are several different specific types of exceptions built in to Python,
# and you should try to use the most specific type possible when catching
# exceptions.

# That is, it is possible to catch *any* exception type by not specifying a type
# to catch:
try:
    fail()
except:
    print("I have no idea why that failed!")

# But doing this can make errors very, very hard to find later on. Better to be
# explicit about the type of error you think might occur:
try:
    fail()
except NameError:
    print("Whoops! Forgot to define fail() before I called it!")

# You can save the exception to a variable when you catch it in order to get
# more information out of it:
try:
    fail()
except NameError as e:
    print("The error occured becase", e)
    print("This particular error occurred at line", e.__traceback__.tb_lineno)

# Finally, you can define your own exception types! This is very handy so that
# you can raise them manually somewhere in your code if something unexpected
# happens.

# This funky syntax we haven't seen yet creates a new "class" called MyError
# that inherits all the same behavior as the built-in "Exception" class. But by
# doing this we get to refer to it by its new name, that only exists within our
# code.
class MyError(Exception):
    pass

def fail_on_purpose():
    print("I'm gonna fail!")
    raise MyError

try:
    fail_on_purpose()
except MyError:
    print("It failed, but that's cool, we were prepared!")