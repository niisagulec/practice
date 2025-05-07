from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1 #iki gösterge biri soldan biri sağdan basladi

        while l < r: #göstergeler kesişene kadar devam
            area = (r - l) * min(height[l], height[r]) 
            res = max(res, area) #büyük alan güncellenir

            if height[l] < height[r]: #sol cubuk kısaysa solu ileri al
                l += 1
            else:
                r -= 1 

        return res

# Test senaryosu
sol = Solution()
test_input = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(test_input))  
