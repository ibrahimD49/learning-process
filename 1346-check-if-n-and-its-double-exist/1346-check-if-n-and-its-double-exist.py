class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(0,len(arr)):
            val = arr[i] * 2
            for j in range(0,len(arr)):
                if i!=j and val == arr[j]:
                    return True
        return False
            

        