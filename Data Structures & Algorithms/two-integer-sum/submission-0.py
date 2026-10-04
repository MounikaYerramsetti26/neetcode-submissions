class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            more = target - nums[i]
            if more not in map:
                map[nums[i]] = i
            else:
                return [map[more],i]