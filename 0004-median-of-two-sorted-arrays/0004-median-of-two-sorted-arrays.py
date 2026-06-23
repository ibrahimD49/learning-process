class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        l=sorted(nums1)
        if len(l)%2==0:
            return float((l[int(len(l)/2)-1]+l[int((len(l)/2)+1)-1])/2)
        else:
            return float(l[int((len(l)+1)/2)-1])
        