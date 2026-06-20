class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        check = {}
        for char in s:
            check[char] = check.get(char, 0) + 1

        for char in t:
            if char in check:
                check[char] -= 1
                if check[char] < 0:
                    return False
            else:
                return False
        return True
                
        
            