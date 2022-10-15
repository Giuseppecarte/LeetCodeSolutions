'''
        Submission performance 

- 2094/2094 Test Cases 

- Runtime: 197ms 
 
- Memory Usage: 14.2 MB

        Submission Results 

- Memory better than 39.17% of the total submissions

- Runtime better than 67.15% of the total submissions 

'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted([*nums1, *nums2])
        if len(merged)%2 ==0:
            mediumPointA = int(len(merged)/2)-1
            mediumPointB = mediumPointA+1 
            median = (merged[mediumPointA] + merged[mediumPointB]) / 2
        else:
            mediumPoint = int(len(merged)/2)
            median = merged[mediumPoint]
        return median
