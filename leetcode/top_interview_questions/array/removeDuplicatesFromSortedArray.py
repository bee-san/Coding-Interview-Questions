class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        # We use while loop to try and cut down on 2 loops
        while counter < (len(nums) - 1):
            # if current counter is the same as the next one
            # removr current
            if nums[counter] == nums[counter + 1]:
                nums.remove(nums[counter])
            else:
                # else they are not the same, so counter +=1 
                counter += 1
        return len(nums)
