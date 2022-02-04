# Improving the Caesar cipher

text = input("Enter text to encrypt: ")
while True:
    shift = input ("shift value (an integer number from the range 1..25): ")
    try:
        if int(shift) >= 1 and int(shift) <=25:
            break
    except:
        continue 
cipher = ""
for ch in text:
    if not ch.isalpha():
        cipher += ch
    else:
        new_ord = ord(ch) + int(shift)
        if ch.isupper() and chr(new_ord) > "Z":
            new_ord = int(shift) - (ord("Z")- ord(ch)) - 1 + ord ("A")
            new_ch =chr(new_ord)
        elif  ch.islower() and chr(new_ord) > "z":   
            new_ord = int(shift) - (ord("z")- ord(ch)) - 1 + ord ("a")
        new_ch =chr(new_ord)
        cipher += new_ch
print(cipher)        








