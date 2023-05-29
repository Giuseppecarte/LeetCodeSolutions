'''Find the Index of the First Occurrence in a String

- Runtime: 42 ms 

- Memory Usage: 16.3 MB

        Subission Results 

- Runtime better than 47.50% of the total submissions 

- Memory better than 38.35% of total submissions

'''


class Solution:
    
    def strStr(self,haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        
        except:
            return -1
