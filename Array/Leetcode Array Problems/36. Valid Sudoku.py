"""
Question:
        Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        Note:

        A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        Only the filled cells need to be validated according to the mentioned rules.
        

        Example 1:


        Input: board = 
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
        Output: true
        Example 2:

        Input: board = 
        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
        Output: false
        Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
        

        Constraints:

        board.length == 9
        board[i].length == 9
        board[i][j] is a digit 1-9 or '.'.
"""


"""
Method 1: 
        Loop through the array 'board'. 
        For each number in 'board', check if that number is there again in that paticular row or column or box.
        If it is there in the row, column or box, then it is a duplicate. Hence, return False
        If it is not there, continue the loop.
        If no such duplicates exist, return True.
Time Complexity: O(9^3)
Space Complexity: O(1)
"""
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        def list_to_box(m,n):
            s = 0
            t = 0
            if m > 5:
                s = 6
            elif m > 2:
                s = 3
            if n > 5:
                t = 6
            elif n > 2:
                t = 3
            return s,t
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    number = board[i][j]
                    boolean = False
                    boolean2 = False
                    for m in range(9):
                        if number == board[m][j]:
                            if boolean:
                                return False
                            boolean = True
                        if number == board[i][m]:
                            if boolean2:
                                return False
                            boolean2 = True
                    s,t = list_to_box(i,j)
                    boolean = False
                    for m in range(s, s+3):
                        for n in range(t, t+3):
                            if number == board[m][n]:
                                if boolean:
                                    return False
                                boolean = True
                                
        return True
                
        
"""
Method 1: 
        Loop through the array 'board'. 
        
        For each row in 'board', check if that value exists in the dictionary_rows.
        If it already exists in the dictionary_rows, then it is a duplicate. Therefore, return False
        If it does not exist in the dictionary_rows, then store it in the dictionary_rows.
        
        Repeat the above procedure for columns and box(or grid)

        If no such duplicates exist, return True.
Time Complexity: O(9^2)
Space Complexity: O(9)
"""
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        s = 0
        t = 0
        for i in range(9):        
            dictionary_box = {}
            dictionary_rows = {}
            dictionary_cols = {}
            for j in range(9):
                if board[i][j] in dictionary_rows:
                    return False
                if board[i][j] != ".":
                    dictionary_rows[board[i][j]] = 1
            for j in range(9):
                if board[j][i] in dictionary_cols:
                    return False
                if board[j][i] != ".":
                    dictionary_cols[board[j][i]] = 1
            for j in range(s,s+3):
                for k in range(t,t+3):
                    if board[j][k] in dictionary_box:
                        return False
                    if board[j][k] != ".":
                        dictionary_box[board[j][k]] = 1
            t += 3
            if t == 9:
                s += 3
                t = 0
        return True