class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Convert the list into a set, which automatically removes any duplicates.
        # For example: [1, 2, 2, 3] becomes {1, 2, 3}
        num = set(nums)

        # If the length of the set is the same as the original list,
        # it means there were no duplicates (since nothing was removed).
        if len(num) == len(nums):
            return False  # No duplicates found

        # If the lengths differ, some items were removed = duplicates existed
        # Simple Way to Think About It:
        # "If putting all the numbers in a set shortens the list, then some numbers must have been repeated."
        return True

        # Time Complexity: O(n) — each element is added to the set once
        # Space Complexity: O(n) — in the worst case, all elements are unique and stored in the set
