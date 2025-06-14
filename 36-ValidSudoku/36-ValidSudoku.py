# Last updated: 6/14/2025, 10:34:12 PM
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [0] * 9
        columns = [0] * 9
        boxes = [0] * 9
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                num = ord(board[i][j]) - ord('1')  # Convert '1'-'9' to 0-8
                mask = 1 << num                    # Create bitmask for the number
                box_index = (i // 3) * 3 + (j // 3)
                
                # Check if the number is already set in the row, column, or box
                if (rows[i] & mask) or (columns[j] & mask) or (boxes[box_index] & mask):
                    return False
                
                # Mark the number in the row, column, and box
                rows[i] |= mask
                columns[j] |= mask
                boxes[box_index] |= mask
        
        return True