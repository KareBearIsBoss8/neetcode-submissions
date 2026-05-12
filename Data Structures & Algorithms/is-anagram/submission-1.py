class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_chars = dict()
        t_chars = dict()

        for i in range(len(s)):
            s_chars[s[i]] = s_chars.get(s[i], 0) + 1
            t_chars[t[i]] = t_chars.get(t[i], 0) + 1
        
        for i in s_chars:
            if i not in t_chars or s_chars[i] != t_chars[i]:
                return False
        return True