# We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.

# Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

# For example:

# if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
# if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)


text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")

text1 = text1.lower()
text2 = text2.lower()

result = "Yes"
start = 0
for ch in text1:
    found = text2.find(ch, start)
    if found == -1:
        result = "No"
        break
    else:
        start = found+1
print(result)