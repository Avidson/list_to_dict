
from list_to_dicts import convert_list_to_dict


list1 = [1, 2, 3, 4, 'five']
list2 = ['One', 'two', 'three', 'four', 5]

new_file = convert_list_to_dict(list1, list2)
print(new_file)
