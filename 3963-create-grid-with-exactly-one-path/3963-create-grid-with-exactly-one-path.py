class Solution:

  def createGrid(self, m: int, n: int) -> list[str]:
    # Pure grid ko '#' se initialize karein
    grid = [['#' for _ in range(n)] for _ in range(m)]

    # Pehle row ke saare cells ko '.' banayein
    for j in range(n):
      grid[0][j] = '.'

    # Aakhri column ke saare cells ko '.' banayein
    for i in range(m):
      grid[i][n - 1] = '.'

    # Lists ko strings mein convert karke return karein
    return [''.join(row) for row in grid]
