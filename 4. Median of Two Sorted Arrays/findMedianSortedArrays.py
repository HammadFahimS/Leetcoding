class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Calculate lengths of the input arrays
        m = len(nums1)
        n = len(nums2)
        m_n = m + n  # Total length of the combined arrays
        
        # Check if the total number of elements is even
        if m_n % 2 == 0:
            merged = []  # List to hold merged array
            m_ptr = 0  # Pointer for nums1
            n_ptr = 0  # Pointer for nums2
            
            # Merge the arrays while keeping them sorted
            for i in range(m + n):
                if m_ptr == m:  # All elements from nums1 are merged
                    merged.extend(nums2[n_ptr:])  # Add remaining nums2 elements
                    break
                if n_ptr == n:  # All elements from nums2 are merged
                    merged.extend(nums1[m_ptr:])  # Add remaining nums1 elements
                    break
                # Compare elements and merge in sorted order
                if nums1[m_ptr] > nums2[n_ptr]:
                    merged.append(nums2[n_ptr])
                    n_ptr += 1
                elif nums1[m_ptr] < nums2[n_ptr]:
                    merged.append(nums1[m_ptr])
                    m_ptr += 1
                elif nums1[m_ptr] == nums2[n_ptr]:  # If elements are equal, add both
                    merged.append(nums2[n_ptr])
                    merged.append(nums1[m_ptr])
                    m_ptr += 1
                    n_ptr += 1
            # Calculate the median for even total number of elements
            median = (merged[m_n//2 - 1] + merged[m_n//2]) / 2.0
            return median
        else:  # If the total number of elements is odd
            merged = []  # List to hold merged array
            m_ptr = 0  # Pointer for nums1
            n_ptr = 0  # Pointer for nums2
            
            # Similar merging process as the even case
            for i in range(m + n):
                if m_ptr == m:
                    merged.extend(nums2[n_ptr:])
                    break
                if n_ptr == n:
                    merged.extend(nums1[m_ptr:])
                    break
                if nums1[m_ptr] > nums2[n_ptr]:
                    merged.append(nums2[n_ptr])
                    n_ptr += 1
                elif nums1[m_ptr] < nums2[n_ptr]:
                    merged.append(nums1[m_ptr])
                    m_ptr += 1
                elif nums1[m_ptr] == nums2[n_ptr]:
                    merged.append(nums2[n_ptr])
                    merged.append(nums1[m_ptr])
                    m_ptr += 1
                    n_ptr += 1
            # Calculate the median for odd total number of elements
            median = merged[(len(merged) - 1) // 2]
            return median
