# Median of Two Sorted Arrays Solution
## Problem Statement
The "Median of Two Sorted Arrays" problem is a classical challenge that requires finding the median of two sorted arrays. Given two sorted arrays, nums1 and nums2, of size m and n, respectively, the task is to find the median value in a merged array that is still sorted. This problem has been labeled as 'Hard' due to the constraints that aim for an efficient solution with a time complexity of `O(log (m+n))`.

## Solution Overview
The solution involves merging the two arrays while maintaining their sort order and then calculating the median. The approach is efficient in scenarios where both arrays are large and sorted. By merging only enough of the arrays to find the median, the solution avoids the full merge cost of `O(m+n)` typically associated with concatenating and sorting two arrays.

## Detailed Explanation
### Merging Arrays:
The function starts by initiating two pointers, one for each array. It then iterates through the arrays, comparing the current elements pointed to by the pointers and appending the smaller (or equal) element to a new list.
### Calculating Median:
Once enough elements have been merged (i.e., half of the total length of both arrays), the median is calculated. The median is the middle element if the total number of elements is odd. If even, it is the average of the two middle elements.

## Complexity Analysis
Time Complexity: The time complexity is `O(m+n)`, which, while not meeting the optimal `O(log (m+n))` suggested in the problem constraints, is efficient for the merged length due to direct comparison without complete sorting.
Space Complexity: The space complexity is `O(m+n)` due to the storage required for the merged array.

## Results
* Runtime: 61 ms, beating 66.41% of Python submissions.
* Memory Usage: 11.75 MB, better than 67.99% of Python submissions.
