'''
        Submission performance

- Runtime: 55 ms 

- Memory Usage: 13.9MB

        Subission Results 

- Runtime better than 35.39% of the total submissions 

- Memory better than 60.91% of total submissions

'''

class Solution:
    ROMAN_DICT = {"I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000}
    
    def ascendant(self,numbers:list)->bool:
        ascendant_list = True
        if len(numbers)>1:
            for index in range(len(numbers)-1):
                if numbers[index] < numbers[index+1]:
                    ascendant_list = False
        return ascendant_list
    
    def romanToInt(self,s:str)->int:
        numerical_list = [self.ROMAN_DICT.get(i) for i in s]
        if self.ascendant(numerical_list):
            return sum(numerical_list)
        
        else:
            numerical_list += [0]

            total = 0 
            index = 0

            while index <= len(numerical_list)-2:
                if numerical_list[index] >= numerical_list[index+1]:
                    total += numerical_list[index]
                    index += 1
                else:
                    difference = numerical_list[index+1] - numerical_list[index]
                    total += difference
                    index += 2

            return total