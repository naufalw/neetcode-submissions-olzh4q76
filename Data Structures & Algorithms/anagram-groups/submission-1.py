from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for i in strs:
            for j in res:
                if Counter(j[0]) == Counter(i):
                    j.append(i)
                    break
            else:
                res.append([i])
            

        print(res)

        return res