class Solution:
    def twoSumNaive(self, nums: list[int], target: int) -> list[int]:
        """O(n^2) Solution as discussed in part 2-A."""
        for i in range(len(nums)):
            # No need to check backwards in the list, since we already checked those possible pairs on
            # previous iterations of the outer for loop.
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # Constraints tell us that a solution MUST exist - so we will not make any kind of edge-case/default-case.

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """O(n) Solution as discussed in part 2-B."""

        # Recall that you can use integers directly as keys in a Python dict.
        seen_nums = {}

        for i in range(len(nums)):
            # Calculate our difference.
            diff = target - nums[i]

            try:
                # Check the dictionary for our difference and return the indices if we can find it.
                return [seen_nums[diff], i]
            except KeyError:
                # If we're unable to find our difference in our dictionary, a KeyError will be raised - so, we'll know
                # that we haven't seen the matching integer before.

                # Store the int:index as a key:value pair.
                seen_nums[nums[i]] = i

        # Constraints tell us that a solution MUST exist - so we will not make any kind of edge-case/default-case.
