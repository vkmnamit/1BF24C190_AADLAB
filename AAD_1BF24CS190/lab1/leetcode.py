class Solution:
    def removeDuplicates(self, nums):
        position=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[position]=nums[i]
                position+=1
        return position

