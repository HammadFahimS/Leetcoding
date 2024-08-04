class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Sort the list to facilitate the two-pointer technique.
        nums.sort()
        
        # Initialize the length of the list for usage in loops.
        length = len(nums)
        
        # Initialize the closest sum to the sum of the first three elements.
        closest = nums[0] + nums[1] + nums[2]
        
        # Initialize the minimum distance to a large number.
        minDist = float('inf')
        
        # Early return if the first three elements sum up to the target.
        if closest == target:
            return closest
        
        # Iterate over the array, considering each element as the first element of the triplet.
        for i in range(0, length - 2):
            # Two pointers initialized.
            j = i + 1  # Second element of the triplet.
            k = length - 1  # Third element of the triplet.
            
            # Use a while loop to explore pairs with the current first element.
            while j < k:
                a = nums[i]
                b = nums[j]
                c = nums[k]
                
                # Calculate the sum of the triplet.
                three_sum = a + b + c
                
                # If the sum is exactly equal to the target, return it immediately.
                if three_sum == target:
                    return target
                
                # Adjust pointers based on how the sum compares to the target.
                if three_sum < target:
                    j += 1  # Increase the sum by moving the left pointer right.
                else:
                    k -= 1  # Decrease the sum by moving the right pointer left.
                
                # Calculate the distance of the current sum from the target.
                dist = abs(three_sum - target)
                
                # If the current distance is less than the minimum found so far,
                # update the closest sum and the minimum distance.
                if dist < minDist:
                    closest = three_sum
                    minDist = dist
        
        # After examining all possible triplets, return the closest sum found.
        return closest
