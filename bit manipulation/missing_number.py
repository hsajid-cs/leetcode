class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Approach: Bitwise XOR

        Time Complexity: O(n)
        - We iterate through the list twice: once to XOR all indices (0 to n)
          and once to XOR the elements of the array.
        - Total time is linear in the size of the input list.

        Space Complexity: O(1)
        - We use only a constant amount of extra space (two integer variables).
        """

        n = len(nums)

        # XOR of all numbers from 0 to n (inclusive)
        xor_all = 0
        for i in range(n + 1):
            xor_all ^= i  # Step 1: XOR all indices

        # XOR of all elements in the input list
        xor_nums = 0
        for num in nums:
            xor_nums ^= num  # Step 2: XOR all numbers in the list

        # The missing number is the difference between the two XOR results
        # Because x ^ x = 0 and x ^ 0 = x
        return xor_all ^ xor_nums
