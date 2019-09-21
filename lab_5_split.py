def mysplit(strng):
    # if empty or whitespace, return empty string
    if len(strng) == 0:
        return []

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
