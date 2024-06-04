list_of_values = [1, 2]
foot = 3.28084

def convert_units_with_while(list_of_values):
    i = 0
    translation_foot = []
    
    while i <= len(list_of_values):
        translation = list_of_values[-1 + 1] * foot
        translation_foot.append(translation)
    
    print(translation_foot)
convert_units_with_while(list_of_values)
        