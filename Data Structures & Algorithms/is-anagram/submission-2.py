class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        for char in range(len(s)):
            count_s[s[char]] = 1 + count_s.get(s[char], 0)
            count_t[t[char]] = 1 + count_t.get(t[char], 0)
        return count_s == count_t