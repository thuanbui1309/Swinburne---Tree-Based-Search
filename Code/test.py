my_dict = {'b': 1, 'a': 3, 'c': 2}

# Sắp xếp theo khóa
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_dict)


