def create_number(string):
    try:
        number = int(string)
    except ValueError:
        print("Error : number should be in range (0..9)")
        return None
    except KeyboardInterrupt:
        print("are you frustated?")
        return None
    # memberikan output 3 col per number
    if number == 0:
        return ['###',
                '# #',
                '# #',
                '# #',
                '###']
    if number == 1:
        return ['  #',
                '  #',
                '  #',
                '  #',
                '  #']
    if number == 2:
        return ['###',
                '  #',
                '###',
                '#  ',
                '###']
    if number == 3:
        return ['###',
                '  #',
                '###',
                '  #',
                '###']
    if number == 4:
        return ['# #',
                '# #',
                '###',
                '  #',
                '  #']
    if number == 5:
        return ['###',
                '#  ',
                '###',
                '  #',
                '###']
    if number == 6:
        return ['###',
                '#  ',
                '###',
                '# #',
                '###']
    if number == 7:
        return ['###',
                '  #',
                '  #',
                '  #',
                '  #']
    if number == 8:
        return ['###',
                '# #',
                '###',
                '# #',
                '###']
    if number == 9:
        return ['###',
                '# #',
                '###',
                '  #',
                '###']


def enter_number(string):
    if string.lower() == "x":
        print("so long...")
        return False
    if not string.isnumeric():
        print("Error: entry not allowed. Only input numbers or X to exit")
        return True
    
    displays = []
    for s in string:
        displays.append(create_number(s))

    for i in range(0,5):
        for d in displays:
            print(d[i], end=" ") 
        print()
    return True

entry_led = True
while entry_led:
    entry_led = enter_number(input("Masukan nomer :"))




