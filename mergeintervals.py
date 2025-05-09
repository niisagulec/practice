
import unittest
from typing import List

# Çözüme ait kod
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

# Test sınıfı
class TestMergeIntervals(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])

    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.merge([[1,4],[4,5]]), [[1,5]])

    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.merge([[1,4],[0,2],[3,5]]), [[0,5]])

    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.merge([[1,4],[5,6]]), [[1,4],[5,6]])

    def test_single_interval(self):
        sol = Solution()
        self.assertEqual(sol.merge([[2,3]]), [[2,3]])

if __name__ == "__main__":
    unittest.main()
