
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # Sonuç dizisi
        
        # Prefix çarpımı: soldan sağa
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Suffix çarpımı: sağdan sola
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer

s = Solution()
print(s.productExceptSelf([1,2,3,4]))  
print(s.productExceptSelf([2,3,4,5]))  
print(s.productExceptSelf([0,1,2,3]))  
