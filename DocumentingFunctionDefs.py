def my_func(a):
    """some useful information"""


    # do some stuff
    my_list = [a*1, a*2, a*3]
    return my_list

if __name__ == "__main__":
    a, b, c  = my_func(4)

    print(a)
    print(b)
    print(c)
    print(my_func.__doc__)
