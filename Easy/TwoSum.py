'''
        Submission performance 

- 57/57 Test Cases 

- Runtime: 1120ms 
 
- Memory Usage: 14.9 MB

        Submission Results 

- Memory better than 78.06% of the total submissions

- Runtime better than 35.53% of the total submissions 

'''

class Solution:
    def twoSum(self, nums, target):    
        def solve_equation(value,target=target):
            solution = target - value
            return [value,solution]

        reducedMap = [i for i in map (solve_equation,nums) if i[1] in nums]
        for i in reducedMap:
            if i[0] == i[1]:
                if nums.count(i[0]) == 1:
                    reducedMap.pop(reducedMap.index(i))

        reducedMap = reducedMap[0]

        firstValue = reducedMap[0]
        secondValue = reducedMap[1]

        firstIndex = nums.index(firstValue)

        if firstValue != secondValue:
            secondIndex = nums.index(secondValue)

        else:
            secondIndex = [i for i,x in enumerate(nums) if x == secondValue and i != firstIndex][0]


        return [firstIndex, secondIndex]


