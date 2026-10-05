class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(0,n):
            for j in range(0,n):
                if i != j and nums[i] == nums[j] and i<j:
                    count+=1
        return count
        