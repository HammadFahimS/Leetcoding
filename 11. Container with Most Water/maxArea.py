class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Initialize two pointers, one at the beginning (left_wall) and one at the end (right_wall) of the height list.
        left_wall = 0
        right_wall = len(height) - 1
        # Initialize maximum area to 0.
        maximum = 0

        # Use a loop to iterate until the two pointers meet.
        while left_wall < right_wall:
            # Calculate the height of the left and right walls.
            left_wall_height = height[left_wall]
            right_wall_height = height[right_wall]
            # Calculate the area between the two walls, which is the product of the minimum of two heights and the distance between them.
            litres = min(left_wall_height, right_wall_height) * (right_wall - left_wall)
            # Update the maximum area found so far.
            maximum = max(maximum, litres)
            
            # Move the pointer that points to the shorter wall, to potentially find a larger area.
            if right_wall_height < left_wall_height:
                right_wall -= 1
            elif right_wall_height > left_wall_height:
                left_wall += 1
            else:  # If both heights are the same, move both pointers.
                left_wall += 1
                right_wall -= 1

        return maximum
