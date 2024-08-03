class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Helper function to sort the list using insertion sort.
        def sort_list(arr, n):
            n = len(arr)
            if n <= 1:
                return
            for i in range(1, n):
                key = arr[i]
                j = i - 1
                # Move elements of arr[0..i-1], that are greater than key,
                # to one position ahead of their current position.
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
        
        # Get the length of the input list.
        length = len(nums)
        # Sort the input list in-place.
        sort_list(nums, length)
        
        # Initialize the list to store the result triplets.
        zero_sums = []
        # Iterate through the list, taking each number as a possible first element of triplet.
        for i in range(length - 2):
            # Pointers for the second and third elements.
            first = i + 1
            last = length - 1
            
            # Iterate through the array to find valid triplets.
            while first < last:
                # Check to avoid using the same element for the triplet.
                if i == first or i == last or first == last:
                    first += 1
                    last -= 1
                    continue
                
                # Current triplet elements.
                a = nums[i]
                b = nums[first]
                c = nums[last]
                
                # Calculate the sum of the triplet.
                three_sum = a + b + c
                
                # Check if the sum is zero and handle accordingly.
                if three_sum == 0:
                    # Check for duplicates before adding the triplet.
                    if [a, b, c] not in zero_sums:
                        zero_sums.append([a, b, c])
                    # Move the pointers to find the next potential triplet.
                    first += 1
                    last -= 1
                # If the sum is greater than zero, decrease the sum.
                elif three_sum > 0:
                    last -= 1
                # If the sum is less than zero, increase the sum.
                else:
                    first += 1
        
        # Return all found triplets that sum up to zero.
        return zero_sums
