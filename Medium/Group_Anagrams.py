'''
        Submission performance 

- 57/57 Test Cases 

- Runtime: 190ms 
 
- Memory Usage: 22.4 MB

        Submission Results 

- Memory better than 5.5% of the total submissions

- Runtime better than 9.83% of the total submissions 

'''


import hashlib

from typing import List
from collections import Counter

class Solution:
    def dictionary_to_hash(self,dict_ : dict) -> str:
        string = ""
        for key,value in sorted(dict_.items(), key=lambda pair: pair[0], reverse=False):
            string += str(key)+str(value)
        return hashlib.sha256(string.encode('utf-8')).hexdigest()
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        structures_dict = {}
        sublist = []

        index = 0
        for word in strs:
            hash_key = self.dictionary_hash(Counter(word))
            
            if not hash_key in structures_dict.keys():
                structures_dict[hash_key] = index
                sublist.append([word])
                index += 1
            else:
                sublist_index = structures_dict[hash_key]
                sublist[sublist_index] += [word]
        return sublist