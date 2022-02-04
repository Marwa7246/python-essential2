# Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

# Each digit is constructed from 13 LEDs (some lit, some dark, of course)  
# Note: the number 8 shows all the LED lights on.

# Your code has to display any non-negative integer number entered by the user.

# Tip: using a list containing patterns of all ten digits may be very helpful.

pattern = [
'''
# # #
#   #
#   #
#   #
# # #''',
'''
    #
    #
    #
    #
    #''',
'''
# # #
    #
# # #
#    
# # #''',
'''
# # #
    #
# # #
    #
# # #''',
'''
#   #
#   #
# # #
    #
    #''',
'''
# # #
#    
# # #
    #
# # #''',
'''
# # #
#    
# # #
#   #
# # #''',
'''
# # #
    #
    #
    #
    #''',
'''
# # #
#   #
# # #
#   #
# # #''',
'''
# # #
#   #
# # #
    #
# # #''',
] 
while True:
    try:
        num = input("Enter a positive integer number: ")
        num_pattern=[]       
        for dig in num:
            x =pattern[int(dig)]
            x = x.lstrip("\n")
            x= x.split("\n")
            num_pattern.append(x)
        for i in range(5):
            for j in range(len(num_pattern)):
                print (num_pattern[j][i], end="  ")
            print()
        repeat = input("Try again?(y/n) ")
        if repeat != "y" and repeat != "Y":
            break
    except:
        print("invalid entry")