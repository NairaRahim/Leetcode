class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap={}
        for char in magazine:
            hashmap[char]=1+hashmap.get(char,0)
        
        for char in ransomNote:
            if char not in hashmap or hashmap[char]<=0:
                return False
            hashmap[char]-=1
        
        return True