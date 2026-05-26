from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            if res.get(tuple(sorted(i)), None):
                res[tuple(sorted(i))].append(i)
            else:
                res[tuple(sorted(i))] = [i]

        return list(res.values())