'''Remove Letter To Equalize Frequency

- Runtime: 41 ms 

- Memory Usage: 16.44 MB

        Subission Results 

- Runtime better than 18.36% of the total submissions 

- Memory better than 76.90% of total submissions

'''

from collections import Counter
class Solution:

    def _remove_letter(self, int:int, list_:list) -> list:
        list_[int][1] -= 1
        return list_

    def equalFrequency(self, word:str) -> bool:
        most_common = Counter(word).most_common()

        possible = False
        for index in range(len(most_common)):
            mutable_list = self._remove_letter(index,[list(_) for _ in most_common])
            values = set([_[1] for _ in mutable_list if _[1] != 0])
            if len(values) == 1:
                possible = True
                break
            else:
                pass
        return possible                
