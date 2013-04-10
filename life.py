def my_func(some_list):
    local_list = some_list[:]
    local_list.append(4)
    return local_list

my_list = [1,2,3]
my_func(my_list)
#print(my_list)
print(my_list[:])

re.sub(r'[^a-zA-Z0-9]', '')
