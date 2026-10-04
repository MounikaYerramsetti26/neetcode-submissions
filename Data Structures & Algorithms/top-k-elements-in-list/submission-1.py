class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}
        ans = []

        for val in nums:
            if val in freq:
                freq[val] += 1
            else:
                freq[val] = 1 
            
        sorted_freq = dict(sorted(freq.items(),key = lambda item:item[1], reverse = True))

        for key in sorted_freq.keys():
            ans.append(key)
            if len(ans) == k:
                break
        
        return ans
            

