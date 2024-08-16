from typing import List
from itertools import combinations

candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 30





class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        print('Sorting')
        values = sorted([_ for _ in candidates if _ <= target])
        print('End of sort')
        results = []

        # If the sum of all the values is less than target it does not make sense to check them
        if sum(values) >= target:
            for size in range(1,len(values)+1):
                print(size)
                # it does not make sense to keep looking if that given a size of array the minimum combination of values is higher than the target
                min_combination_value = sum(values[:size])
                max_combination_value  = sum(values[-size:])

                if min_combination_value <= target and max_combination_value >= target:
                    if len(set(values)) > 1:
                        combination_list = set(combinations(values,size))

                        for ith_comb in combination_list:
                            if sum(ith_comb) == target:
                                results.append(ith_comb)
                    else:
                        results.append([values[0]]*(target//values[0]))

        return results
    

print(Solution().combinationSum2(candidates=candidates, target=target))