class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        if len(s) != len(t):
            return False

        for char in s:
            freq[char] =  1 + freq.get(char,0)
        
        for char in t:
            if char not in freq:
                return False
            freq[char] -= 1

        return all(val == 0 for val in freq.values())
        
