class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}
        

        for val in nums:
            freq[val] = freq.get(val,0)+1

        sorted_freq = sorted(freq.items(),key = lambda item:item[1], reverse = True)

        return [key for key,count in sorted_freq[:k]]
            

