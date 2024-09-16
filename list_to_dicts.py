import sys  

""" 
    This lines of code aims at creating a python dictionary object using the 
    items from two different python lists.

    if you wish to add to the code base, feel free to do that.
 """

def convert_list_to_dict(list_1, list_2):

    try:
        converted_item = dict(zip(list_1, list_2))

        print(f'No. of items on this list is: {len(list_1)}')
        print(f'No. of items on this list is: {len(list_2)}')

        for items in range(len(list_1)) and range(len(list_2)):
            if len(list_1) > len(list_2):
                print('There is a mismatch in items quantity. The number of items in first list is greater')
                continue
            elif len(list_1) < len(list_2):
                print('There is a mismatch in items quantity. The number of items in second list is greater')
                continue
            elif len(list_1) == len(list_2):
                return converted_item

        return converted_item

    except SystemError or SyntaxError as e:
        sys.exit(f'error raised says - {e}')

if __name__ == '__main__' :
    convert_list_to_dict

         