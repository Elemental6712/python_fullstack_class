def bracket_balance(symbols):

    if len(symbols) % 2 != 0 or len(symbols) == 0:
        return False
    
    couples = {'(': ')', '{': '}', '[': ']'}
    check_list = []

    for i in symbols:
        
        if i in couples.keys():
            check_list.append(i)
        
        elif i in couples.values():
            if len(check_list) < 1:
                return False
            last_character = check_list.pop()
        
            if couples[last_character] != i:
                return False

    if len(check_list) == 0:
        return True

print(bracket_balance('([]{}{})'))
print(bracket_balance(']'))
print(bracket_balance('{}['))
print(bracket_balance('{({[{]}})}'))
print(bracket_balance(""))