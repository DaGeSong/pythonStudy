
# IBAN Validator.
# (step 1) Check that the total IBAN length is correct
# (step 2) Move the four initial characters to the end of the string(i.e., the country code and the check digits)
# (step 3) Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11 ... Z = 35
# (step 4) Interpret the string as a decimal integer and compute the remainder of that number on division by 97 If the remainder is 1, the check digit test is passed and the IBAN might be valid.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ', '')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    print(iban)
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    print(iban2)
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")
