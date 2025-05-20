
from typing import List
import unittest

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # num -> index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
        return []

# Test senaryoları
class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_example2(self):
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])

    def test_example3(self):
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])

    def test_example4(self):
        self.assertEqual(self.solution.twoSum([1, 5, 3, 7], 8), [0, 3])

if __name__ == "__main__":
    unittest.main()
