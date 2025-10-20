import bisect
from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums2.sort()

        def count_le(value: int) -> int:
            total_count = 0
            for n1 in nums1:
                if n1 > 0:
                    count = bisect.bisect_right(nums2, value / n1)
                    total_count += count
                elif n1 < 0:
                    count = len(nums2) - bisect.bisect_left(nums2, value / n1)
                    total_count += count
                else:
                    if value >= 0:
                        total_count += len(nums2)
            return total_count

        low = -10**10 - 1
        high = 10**10 + 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if count_le(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans

if __name__ == '__main__':
    solver = Solution()

    nums1_1 = [2, 5]
    nums2_1 = [3, 4]
    k_1 = 2
    result_1 = solver.kthSmallestProduct(nums1_1, nums2_1, k_1)
    print(f"Example 1:")
    print(f"Input: nums1 = {nums1_1}, nums2 = {nums2_1}, k = {k_1}")
    print(f"Output: {result_1}")
    print("-" * 20)

    nums1_2 = [-4, -2, 0, 3]
    nums2_2 = [2, 4]
    k_2 = 6
    result_2 = solver.kthSmallestProduct(nums1_2, nums2_2, k_2)
    print(f"Example 2:")
    print(f"Input: nums1 = {nums1_2}, nums2 = {nums2_2}, k = {k_2}")
    print(f"Output: {result_2}")
    print("-" * 20)

    nums1_3 = [-2, -1, 0, 1, 2]
    nums2_3 = [-3, -1, 2, 4, 5]
    k_3 = 3
    result_3 = solver.kthSmallestProduct(nums1_3, nums2_3, k_3)
    print(f"Example 3:")
    print(f"Input: nums1 = {nums1_3}, nums2 = {nums2_3}, k = {k_3}")
    print(f"Output: {result_3}")
    print("-" * 20)

