
import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        nums: integer listesi
        k: sıralamada kaçıncı en büyük eleman isteniyor
        Return: nums listesindeki k. en büyük eleman
        """

        def partition(left, right, pivot_index):
            pivot_value = nums[pivot_index]
            # Pivotu sağa taşıyoruz
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left

            # Pivottan küçükleri sola alıyoruz
            for i in range(left, right):
                if nums[i] < pivot_value:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # Pivotu doğru yerine koyuyoruz
            nums[right], nums[store_index] = nums[store_index], nums[right]

            return store_index

        # İstediğimiz indeks aslında len(nums) - k
        target = len(nums) - k
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot_index = random.randint(left, right)
            pivot_final_index = partition(left, right, pivot_index)

            if pivot_final_index == target:
                return nums[pivot_final_index]
            elif pivot_final_index < target:
                left = pivot_final_index + 1
            else:
                right = pivot_final_index - 1

# --- Test Senaryoları ---

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    expected1 = 5
    result1 = sol.findKthLargest(nums1, k1)
    print(f"Test 1 - Beklenen: {expected1}, Çıktı: {result1}, {'✅ Passed' if result1 == expected1 else '❌ Failed'}")

    # Test 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    expected2 = 4
    result2 = sol.findKthLargest(nums2, k2)
    print(f"Test 2 - Beklenen: {expected2}, Çıktı: {result2}, {'✅ Passed' if result2 == expected2 else '❌ Failed'}")

    # Test 3
    nums3 = [1]
    k3 = 1
    expected3 = 1
    result3 = sol.findKthLargest(nums3, k3)
    print(f"Test 3 - Beklenen: {expected3}, Çıktı: {result3}, {'✅ Passed' if result3 == expected3 else '❌ Failed'}")