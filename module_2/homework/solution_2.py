def  binary_find_element(list_int, element):
    
    count = True

    while count:
        
        beginning_list = 0
        end_list = len(list_int)
        mid_element = end_list // 2
        
        if end_list == 0:
            return False
            
        elif list_int[mid_element] == element:
            return True

        elif end_list == 1 and list_int[mid_element] != element:
            return False

        elif element > list_int[mid_element]:
            del list_int[beginning_list:mid_element]

        elif element < list_int[mid_element]:
            del list_int[mid_element:end_list]


print(binary_find_element([1, 2, 3, 4, 5, 6, 7], 1))
print(binary_find_element([1, 2, 3, 4, 5, 6, 7], 4))
print(binary_find_element([1, 2, 3, 4, 5, 6, 7, 8], 7))
print(binary_find_element([1, 2, 3, 4, 5, 6, 7], 9))
print(binary_find_element([], 3))
