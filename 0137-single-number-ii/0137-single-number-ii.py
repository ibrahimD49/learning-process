class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = {}

        for word in nums:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
    
        for key,value in freq.items():
            if value == 1:
                return key
    
    

        


        