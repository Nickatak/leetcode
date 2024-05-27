I. Original Text: Add Two Numbers

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

 

    Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]
    Example 3:
        Input: nums = [3,3], target = 6
        Output: [0,1]
 

    Constraints:

        2 <= nums.length <= 104
        -109 <= nums[i] <= 109
        -109 <= target <= 109
        Only one valid answer exists.
    

    Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

II. Explanation.
    A. `twoSumNaive()`
        For a naive brute force approach, we can simply check every possible pair of integers for an answer - but this will require us to look at every element in the array, per each element.  So if we have N elements in the array, we'll have to look at each element (N) and then, for each element, look at all the other elements in the list (N - 1) to compare the sum.  This leaves us with a roughy time complexity of N * (N - 1), as N approaches infinity, the `- 1` becomes negligible, and we end up with a resultant time complexity of `O(n * n)` or `O(n^2)`.  This is slow, but it does work.

    B. `twoSum()`
        For a bit better of an approach, we need to use a little bit of calculation trickery.  Since we know the target, and we'll currently be examing some index, we can simply calculate the difference (target - current_num) in order to find our "possible matching number."  Then we simply need to find a way to check if we've seen said possible matching number.  An easy/good way to do this is to abuse the dictionary (Hash Map) structure's constant lookup time (and conveniently, it'll also allow us to store the original index of the number as the value).  Since we'll only need to touch each element once for a calculation and then a constant-time lookup, we end up with a time complexity of O(n).
