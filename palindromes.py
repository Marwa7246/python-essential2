# palindrome a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.

# Your task is to write a program which:

# asks the user for some text;
# checks whether the entered text is a palindrome, and prints result.
# Note:

# assume that an empty string isn't a palindrome;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent;

# Test data
# Sample input:

# Ten animals I slam in a net

# Sample output:

# It's a palindrome


# Sample input:

# Eleven animals I slam in a net

# Sample output:

# It's not a palindrome

text = input("Enter a text to check: ")
if len(text) == 0:
    print("It is not a palindrome")
else:
    text = text.lower()
    text = text.replace(" ","")
    inverted_text = ""
    for i in range (len(text)):
        inverted_text += text[-1-i]
    print(inverted_text)
    if inverted_text == text:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")




