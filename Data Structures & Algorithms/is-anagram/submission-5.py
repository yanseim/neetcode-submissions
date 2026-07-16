class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()
        for n in set(s):
            s_dict[n]=s.count(n)
        for n in set(t):
            t_dict[n] = t.count(n)
        if s_dict==t_dict:
            return True
        return False