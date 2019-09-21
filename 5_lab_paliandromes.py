import sys

text = input("Check your text : ")

if not text:
    print("Empty string, it's not paliandromes")
    sys.exit()

text = text.lower().replace(" ", "")
for i in range(len(text)//2):
    if text[i] != text[-i-1]:
        print("It's not paliandrom")
        sys.exit()
print("Check OK, it's paliandrom")
