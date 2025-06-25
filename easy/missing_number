class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Let s be the sum of all elements in the list
        s = 0

        # n is the number of elements in the input list
        # Since one number is missing from the range [0, n], the complete range should have (n+1) numbers
        n = len(nums)

        # Calculate the sum of the first n natural numbers (0 to n)
        # Formula: sum = n * (n + 1) / 2
        # This is what the sum should be if no number was missing
        #
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        actual_sum = (n * (n + 1)) / 2

        # Calculate the sum of the given list
        #
        # Time Complexity: O(n) — iterate through the list once
        # Space Complexity: O(1) — just one variable to keep the running sum
        for num in nums:
            s += num

        # The missing number is the difference between expected sum and actual sum
        return actual_sum - s
