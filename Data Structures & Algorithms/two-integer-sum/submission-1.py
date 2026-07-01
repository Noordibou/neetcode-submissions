class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i , n in enumerate(nums):
            y = target - n
            if y in h:
                return [h[y], i]
            h[n] = i