# An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

# Your task is to write a program which:

# asks the user for two separate texts;
# checks whether, the entered texts are anagrams and prints the result.
# Note:

# assume that two empty strings are not anagrams;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent
# Test your code using the data we've provided.

# Test data
# Sample input:

# Listen
# Silent

# Sample output:

# Anagrams


# Sample input:

# modern
# norman

# Sample output:

# Not anagrams

text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")
if len(text1) == 0 or len(text2) == 0:
    print("Not anagrams")
else:
    text1 = text1.lower()
    text1 = text1.replace(" ","")
    text2 = text2.lower()
    text2 = text2.replace(" ","")
    if sorted(text1) == sorted(text2):
        print("Aanagrams")
    else:
        print("Not anagrams")

