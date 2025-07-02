class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Initialize a variable to store XOR result
        xor_el = 0

        # Loop through all numbers in the list
        # XOR each number with xor_el
        # Property of XOR:
        # - a ^ a = 0 (same numbers cancel each other)
        # - a ^ 0 = a (XOR with 0 keeps the number)
        # So, all duplicate numbers cancel out,
        # and only the single (non-duplicate) number remains.
        #
        # Time Complexity: O(n) — we traverse the list once
        # Space Complexity: O(1) — only one variable is used
        for num in nums:
            xor_el ^= num

        # The result is the number that appeared only once
        return xor_el
