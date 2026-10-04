class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = {}

        for word in strs:

            freq = [0] * 26

            for chr in word:
                freq[ord(chr) - ord('a')] += 1 
            
            key = tuple(freq)

            if key not in map:
                map[key] = []
            
            map[key].append(word)
        return list(map.values())
