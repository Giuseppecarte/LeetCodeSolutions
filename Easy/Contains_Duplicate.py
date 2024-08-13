''' Contains Duplicate

- Runtime: 618 ms 

- Memory Usage: 30.8 MB

        Subission Results 

- Runtime better than 5.7% of the total submissions 

- Memory better than 89.86% of total submissions

'''
class Solution:
    def containsDuplicate(self, nums :List[int]) -> bool:
        return len(nums) != len(set(nums))