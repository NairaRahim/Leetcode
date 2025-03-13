class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for ind in set(s):
            print(ind,s.count(ind))
            if s.count(ind) != t.count(ind):
                return False
        return True
        #first method
        # s_freq=dict()
        # t_freq=dict()
        # for char in s:
        #     s_freq[char] = s_freq.get(char,0)+1
        # for char in t:
        #     t_freq[char] = t_freq.get(char,0)+1

        # return s_freq == t_freq
        
        