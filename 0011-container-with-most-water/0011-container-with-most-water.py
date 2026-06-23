class Solution:
    def maxArea(self, height: List[int]) -> int:
      start = 0 
      end = len(height) - 1
      Maxarea = 0
      while (start <= end ):
        breath = end - start
        length = min(height[start],height[end])
        area = length * breath

        Maxarea = max(Maxarea,area)

        if (height[start]<height[end]):
            start+=1
        else :
            end -=1
      return Maxarea