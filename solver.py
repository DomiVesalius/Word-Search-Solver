"""
== WORD SEARCH SOLVING ALGORITHM ==
1. Iterate through all possible letters in the search:
2. For each letter, find the horizontal, vertical, and diagonal groupings.
3. For each grouping, iterate through the words matrix and for each word, check if the word is within
   that grouping.
5. If the word is within that grouping, use .join and .find(word) to find the starting index of the word
"""
from typing import List, Tuple

def get_horizontal(puzzle: List[List[str]], position: Tuple[int, int]) -> List[str]:
   """
   Returns the horizontal grouping for the specified index
   """
   row_index = position[0]
   return puzzle[row_index]

def get_vertical(puzzle: List[List[str]], position: Tuple[int, int]) -> List[str]:
   """
   Returns the vertical grouping for the specified index
   """
   col_index = position[1]
   col = []
   for i in range(len(puzzle)):
      col.append(puzzle[i][col_index])
   return col
   
def get_diagonal(puzzle: List[List[str]], position: Tuple[int, int]) -> Tuple[List[str], List[str]]:
   """
   Returns the two diagonal groupings for the specified index
   """
   y, x = position

   if y > x:
      while x >= 1:
            x -= 1
            y -= 1
   else:
      while y >= 1:
            y -= 1
            x -= 1
   diagonal = []
   while x < len(puzzle) and y < len(puzzle[0]):
      diagonal.append(puzzle[y][x])
      x += 1
      y += 1

   y, x = position
   if y > x:
      while x >= 1:
            x -= 1
            y -= 1
   else:
      while y >= 1:
            y -= 1
            x -= 1
   diagonal2 = []
   while x < len(puzzle) and y < len(puzzle[0]):
      diagonal2.append(puzzle[x][y])
      x += 1
      y += 1 # NOT FINISHED
   
   return (diagonal, diagonal2)

from examples import scientists_search
print(get_diagonal(scientists_search, (3, 1)))
