#Todo
# - represent each 3x3 box with a hash set
# - 0, 1, 2 to represent a columns and rows of hash sets
# -    ^ to get a number's coordinates, get a number from a hash set and do the formula: n / 3, n / 3 (integer division). for example, column 1 row 1 has 4 in the middle. 4/3, 4/3 = 1, 1 => this will be our hash map key for each hash set box

# - if there are any duplicates, return false by checking the following:
# - is r is already in rows map (seen)?
# - is c already in columns map?
# - is the current coordinates already mapped? (ex.: has the current square [1, 1] been mapped already?)
# if any of these is true, then it's not valid.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) # hash map (key = column number and value will be set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r /3, c /3)
        # rows is a hash map and r is our key for coordinates
        for r in range(9): # go through rows and columns
            for c in range(9):
                if board[r][c] == ".":
                    continue # ignore dots since theyre empty space
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[r // 3, c // 3]):
                    return False
                 # update hash maps to keep track of numbers as we go through the columns, rows and squares (9 times for cols & rows and 9 more for each square)
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c]) # saving key
        return True
