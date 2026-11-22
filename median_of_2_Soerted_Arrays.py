class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2       # elements taken from nums1
            j = half - i                  # elements taken from nums2

            nums1_left = nums1[i - 1] if i > 0 else float("-inf")
            nums1_right = nums1[i] if i < m else float("inf")
            nums2_left = nums2[j - 1] if j > 0 else float("-inf")
            nums2_right = nums2[j] if j < n else float("inf")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total % 2:
                    return float(max(nums1_left, nums2_left))
                return (
                    max(nums1_left, nums2_left)
                    + min(nums1_right, nums2_right)
                ) / 2.0

            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1
