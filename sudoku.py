# Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

# each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
# each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
# each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
# If you need more details, you can find them here.

# Your task is to write a program which:

# reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
# outputs Yes if the Sudoku is valid, and No otherwise.
# Test your code using the data we've provided.

# Test data
# Sample input:

# 295743861
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 154938672
# Sample output:

# Yes


# Sample input:

# 195743862
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 254938671
# Sample output:

# No

 


board1 ='''
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672'''

 
board2 ='''
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671'''

def check_pattern(sub_board):
    for num in range(1,10):
        if num not in sub_board:
            return False
    return True

def create_three_by_three_sub_board(list_board, i, j):
    sub_board = []
    for k in range(i, i+3):
        sub_board += list_board[k][j:j+3]
    return sub_board

def sudoko(board):
    result = True
    list_board = board.lstrip().split("\n")
    for row in list_board:
        i = list_board.index(row)
        row = [int(dig) for dig in row]
        list_board[i] = row
    # print(list_board)
    for row in list_board:
        result = check_pattern(row)
        if result == False:
            return False
    # if result == True:
    for j in range(9):
        list_col = [list_board[i][j] for i in range(9) ]
        result = check_pattern(list_col)
        if result == False:
            return False

    # if result:
    for i in range(0, 7, 3):
        for j in range (0, 7, 3):
            sub_board = create_three_by_three_sub_board(list_board, i, j)
            result = check_pattern(sub_board)
            if result == False:
                return False
        # if not result:
        #     break    
    return result

if sudoko(board1): print("Yes")
else: print("No")




