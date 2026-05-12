class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in strs:
            letters = [0]*26
            for j in i:
                letters[ord(j) - ord('a')] += 1
            groups[tuple(letters)].append(i)
        
        res = []
        for i in groups.values():
            res.append(i)
        return res