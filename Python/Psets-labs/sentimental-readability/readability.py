from cs50 import get_string

text = get_string("Text: ")

L = 0
S = 0
W = 1

for i in range(len(text)):
    if text[i].isalpha():
        L += 1
    elif text[i].isspace():
        W += 1
    elif text[i] == '.' or text[i] == '?' or text[i] == '!':
        S += 1

newL = L / W * 100
newS = S / W * 100

index = round(0.0588 * newL - 0.296 * newS - 15.8)

if index < 1:
    print("Before Grade 1")

elif index >= 1 and index <= 16:
    print("Grade %d" % (index))

elif index > 16:
    print("Grade 16+")
