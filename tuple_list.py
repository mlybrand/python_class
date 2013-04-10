list_of_tuples = [(1,2,3),(4,5,6)]
flattened_list = [list(this_tuple) for this_tuple in list_of_tuples]
flattened_list.extend(flattened_list.pop())
flattened_list.reverse()
flattened_list.extend(flattened_list.pop())
flattened_list.sort()

print(flattened_list)

for this_tuple in list_of_tuples:
    print(this_tuple[0])
    print(this_tuple[1])
    print(this_tuple[2])
    print()

list_of_tuples[0]

list_of_tuples[0][0]
