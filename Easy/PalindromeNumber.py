class Solution:
    def isPalindrome(self, x):
        forward = [i for i in str(x)]
        reverse = [i for i in str(x)[::-1]]
        if forward == reverse:
            return True
        else:
            return False
  
'''
        Submission performance

- 11510 / 11510 Test Cases 

- Runtime: 112 ms 

- Memory Usage: 14MB

        Subission Results 

- Runtime better than 53.83% of the total submissions 

- Memory better than ?? 

'''