class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        pt, pb = 0, ROWS - 1
        while pt <= pb:
            row = (pt + pb) // 2
            if target > matrix[row][-1]:
                pt = row + 1
            elif target < matrix[row][0]:
                pb = row - 1
            else:
                break
        if not (pt <= pb):
            return False
        row = (pt + pb) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                # search right
                l = m + 1
            elif target < matrix[row][m]:
                # search left
                r = m - 1
            else:
                return True
        return False