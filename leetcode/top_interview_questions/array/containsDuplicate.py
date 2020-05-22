class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return [True if x == [x + 1] for nums[x] in range(len(nums) - 1)]
