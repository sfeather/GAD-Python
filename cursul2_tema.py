my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
my_list_copy = my_list.copy()
my_list_copy.sort()
print(my_list_copy)
# my_list_copy.sort(reverse=True)
print(my_list_copy[10::-1])
print(my_list_copy[1:10:2])
print(my_list_copy[0:9:2])
print(my_list_copy[2:10:3])
