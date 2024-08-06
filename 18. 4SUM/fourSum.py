class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Get the length of the input list
        length = len(nums)
        # Return empty list if there are less than four numbers
        if length < 4:
            return []
        # If there are exactly four numbers and their sum matches the target, return them
        if length == 4 and sum(nums) == target:
            return [nums]
        # Sort the numbers to facilitate the two-pointer technique
        nums.sort()
        # Initialize a dictionary to store unique quadruplets
        quadruplets = {}
        # Use two nested loops to fix the first two elements
        for i in range(length-3):
            for j in range(i+1, length-2):
                # Initialize two pointers for the remaining two elements
                k, l = j+1, length-1
                # Get the values of the first two fixed elements
                a = nums[i]
                b = nums[j]
                # Iterate while the two pointers do not cross
                while k < l:
                    # Get the values of the elements at the two pointers
                    c = nums[k]
                    d = nums[l]
                    # Calculate the sum of the four elements
                    summation = a + b + c + d
                    # If the sum matches the target, add it to the dictionary
                    if summation == target:
                        quadruplets[tuple([a, b, c, d])] = 1
                        # Move both pointers to look for new possible quadruplets
                        k += 1
                        l -= 1
                    # If the sum is less than the target, move the left pointer to increase the sum
                    elif summation < target:
                        k += 1
                    # If the sum is greater than the target, move the right pointer to decrease the sum
                    else:
                        l -= 1
        # Return the keys of the dictionary as a list of lists
        return [k for k, v in quadruplets.items()]
