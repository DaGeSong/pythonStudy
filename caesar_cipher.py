# asks the user for one line of text to encrypt;
# asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
# prints out the encoded text.

text = input("Enter your message: ")
shift_value = int(input("Please Enter a Shift Value from 1 - 25: "))


def encryped(text, shift_value):
    cipher = ''
    for char in text:
        if char == ' ':
            cipher += char
        elif char.isdigit():
            cipher += char
        elif char.isupper():
            cipher += chr((ord(char) + shift_value - 65) % 26 + 65)
        else:
            cipher += chr((ord(char) + shift_value - 97) % 26 + 97)
    return cipher


while shift_value < 1 or shift_value > 25:
    shift_value = int(input("Please Enter a Shift Value from 1 - 25: "))
else:
    print("The Encrypted string is:\n ", encryped(text, shift_value))
