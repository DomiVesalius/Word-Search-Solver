"""
== WORD SEARCH SOLVING ALGORITHM ==
1. Iterate through all possible letters in the search:
2. For each letter, find the horizontal, vertical, and diagonal groupings.
3. For each grouping, iterate through the words matrix and for each word, check if the word is within
   that grouping.
5. If the word is within that grouping, use .join and .find(word) to find the starting index of the word
"""