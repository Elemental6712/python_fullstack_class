
def find_element(first_argument, second_argument):
    
    true_file, counter, counter_index = 0, 1, 0

    while counter <= len(first_argument):

        if first_argument[counter_index] == second_argument:
            true_file += 1
    
        counter += 1
        counter_index += 1
    
    if true_file >= 1:
        return True
    
    else:
        return False


print(find_element(['max', 'min', 'zero', 'seven'], 'zero'))
print(find_element([1, 2, 3, 4, 5, 6, 7, 8], 7))
print(find_element(['max', 'min', 'zero', 'seven'], 'zeroo'))
print(find_element([1, 2, 3, 4, 5, 6, 7, 8], 9))
print(find_element([1, 2, 3, 4, 5, 6, 7, 8], 'zero'))
print(find_element(['max', 'min', 'zero', 'seven'], 7))