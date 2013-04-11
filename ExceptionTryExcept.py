try:
    x = 7
    #y = 0
    y = 7
    print("foo", (x / y))
except NameError:
    print("Python is case sensitive")
except ZeroDivisionError:
    print("Dividing by zero results in infinity in my opinion :)")
else:
    print("Stuff to happen after try, but before finally, when everything is cool.")
finally:
    print("Cleaning up my mess")
