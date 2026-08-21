class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for row in range(9):
            seen = set()

            for col in range(9):
                num = board[row][col]

                if num == ".":
                    continue

                if num in seen:
                    return False

                seen.add(num)

        # Check columns
        for col in range(9):
            seen = set()

            for row in range(9):
                num = board[row][col]

                if num == ".":
                    continue

                if num in seen:
                    return False

                seen.add(num)

        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):

                seen = set()

                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):

                        num = board[row][col]

                        if num == ".":
                            continue

                        if num in seen:
                            return False

                        seen.add(num)

        return True
board=[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
s=Solution()
s.isValidSudoku(board)