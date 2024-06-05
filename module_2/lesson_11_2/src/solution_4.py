metric_system = ([1, 2], 'meters')
imperial_system = 3.28084

def convert_units_with_while(metric_system):
    count = 1
    unit = metric_system[0]

    while count <= len(unit):
        print(f'{count} meter(s) = {imperial_system * count} foot(feet)')
        count += 1

convert_units_with_while(metric_system)