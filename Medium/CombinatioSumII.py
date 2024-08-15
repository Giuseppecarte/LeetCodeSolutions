from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from itertools import combinations
        if sum(candidates) < target:
            return []
        else:
            # Remove all the values from candidates that are higher than the target
            candidates = list(set([_ for _ in candidates if _ <= target]))
            print(len(candidates), len(list(set(candidates))))
            output = []
            for combination_size in range(1, len(candidates) + 1):
                for combination in combinations(candidates,combination_size):
                    sorted_combination = sorted(list(combination))
                    if sum(sorted_combination) == target and not sorted_combination in output:
                        output.append(sorted_combination)
            return output

'''Time Exceeded'''

candidates = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
target = 27
sol = Solution()
print(sol.combinationSum2(candidates, target))


    