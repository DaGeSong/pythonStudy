# '''
# The task is to write your own function, which behaves almost exactly like the original split() method, i.e.:
# it should accept exactly one argument - a string;
# it should return a list of words created from the string, divided in the places where the string contains whitespaces;
# if the string is empty, the function should return an empty list;
# '''

def mysplit(strng):
    strng = strng.strip()
    list = []
    str = ''
    if strng.isspace() or strng == '':
        return []
    else:
        for letter in strng:
            if letter != ' ':
                str += letter
            else:
                if str != '':
                    list.append(str)
                    str = ''
                    continue
        list.append(str)
        return list


print(mysplit("To   be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the            question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
