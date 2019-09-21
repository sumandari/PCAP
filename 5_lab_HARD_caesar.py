def encoding(ch, shift_value):
     # check if string is not alpha
    if not ch.isalpha():
        return ch
    if ch.islower():
        if ord(ch) + shift_value > 122:
            result = (ord(ch) + shift_value) - 26
        else:
            result = ord(ch) + shift_value
    elif ch.isupper():
        if ord(ch) + shift_value > 90:
            result = (ord(ch) + shift_value) - 26
        else:
            result = ord(ch) + shift_value
    return chr(result)

# asks the user for one line of text to encrypt;
plaintext = input("Enter line of text to encrypt: ")

# asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
valid_shift = False
while not valid_shift:
    try:
        shift_value = int(input("Enter your key number 1..25: "))
        if shift_value < 1 or shift_value > 25:
            print("Error: enter number from 1 to 25: ")
        else:
            valid_shift = True 
    except ValueError:
        print("Error: your entry is not a number: ")

# prints out the encoded text.
for ch in plaintext:
    print(encoding(ch, shift_value), end="")
print()
