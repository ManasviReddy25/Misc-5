# Problem 1: Find Consecutive Ones(https://leetcode.com/problems/max-consecutive-ones-iii/)
# Time Complexity: O(n), i and slow each move forward at most n times
# Space Complexity: O(1), only a few variables used, no extra data structure
# Approach:
# Sliding window with two pointers, slow and i.
# i moves forward, expanding the window to the right.
# Every 0 inside the window costs one flip, so k goes down by 1.
# If k goes below 0, the window has more zeros than flips allowed.
# Shrink from the left (move slow) until it's valid again.
# The window never shrinks below the best valid size found so far, so at the end, n - slow gives the longest valid window length.

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)          # total length of array
        slow = 0                # left edge of the window

        for i in range(n):      # i = right edge of the window
            if nums[i] == 0:
                k -= 1           # spend one flip on this zero

            if k < 0:            # window has too many zeros for flips left
                if nums[slow] == 0:
                    k += 1        # get the flip back, this zero is leaving the window
                slow += 1         # shrink window from the left

        return n - slow          # size of the last (largest) valid window