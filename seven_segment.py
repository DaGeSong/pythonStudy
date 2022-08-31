# Dictionary of (number:7-segment-hash)
dict1 = {
    '0': ('###', '# #', '# #', '# #', '###'),
    '1': ('#', '#', '#', '#', '#'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###')
}

input_string = input(
    "please type your number, or just press enter to exit the program: ")  # '689'

if input_string == '' or input_string.isspace():
    exit()
else:
    # it has to print each row first, not number first
    for row in range(len(dict1['0'])):
        line = []
        for i in input_string:  # '6' '8' '9'
            line.append(dict1[i][row])
        print(' '.join(line))

# it has to print each row first, not number first
num = '0123456789'
for row in range(len(dict1['0'])):
    print(' '.join(tuple(dict1[i][row] for i in num)))
    # print(tuple(dict1[i][row] for i in num))
