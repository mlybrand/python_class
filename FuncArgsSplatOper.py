def sum_nums(*args):
    total = 0
    for arg in args:
        total += arg
    return "The sum of {0} is {1}".format(list(args), total)

