'''
        Submissiom performance

- 124/124 Test Cases 
- Runtime: 15ms 
- Memory Usage: 13.6 MB

        Submission Results

- Memory better than 98.6% of the total submissions

- Runtime better than 58.19% of the total submissions 

'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)>1:
            minChar = min(map(len,strs))

            prefix = ''
            for i in range(1,minChar+1):
                count = 1
                for wordIdx in range(1,len(strs)):
                    if strs[wordIdx-1][:i] == strs[wordIdx][:i]:
                        count+=1
                if count == len(strs):
                    prefix = strs[wordIdx-1][:i]

            return prefix
        else:return strs[0]