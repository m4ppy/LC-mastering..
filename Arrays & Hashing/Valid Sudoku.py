# Approach: Hash Set
# Time Complexity: O(n²) where n = 9 (size of the board)
# Space Complexity: O(n²) for storing hash sets of rows, columns, and squares

# Algorithm:
# 1. Use hash sets to track numbers seen in each row, column, and 3x3 square.
# 2. Traverse the board cell by cell.
#    - Skip empty cells represented by '.'.
#    - Check if the current number exists in the corresponding row, column, or square.
#    - If it does, the board is invalid; return False.
# 3. If no duplicates are found, add the number to the respective sets.
# 4. Return True after validating all cells.

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Hash sets for rows, columns, and 3x3 squares
    rows = collections.defaultdict(set) # Stores numbers seen in each row
    cols = collections.defaultdict(set) # Stores numbers seen in each column
    squares = collections.defaultdict(set) # Stores numbers seen in each 3x3 square

    for r in range(9):
      for c in range(9):
        # Skip empty cells
        if board[r][c] == ".":
          continue

        # Check for duplicates in row, column, and square
        if (board[r][c] in rows[r] or \
         board[r][c] in cols[c] or \
         board[r][c] in squares[(r//3, c//3)]):
          return False

        # Add the number to the corresponding sets
        rows[r].add(board[r][c])
        cols[c].add(board[r][c])
        squares[(r//3, c//3)].add(board[r][c])
        
    return True
