class Solution(object):
    def isAnagram(self, s, t):
        hashmap = {}
        for letter in s:
            if letter not in hashmap:
                hashmap[letter] = 1
            else:
                hashmap[letter] += 1
        for letter in t:
            if letter not in hashmap:
                return False
            else:
                hashmap[letter] -= 1
                if hashmap[letter] == 0:
                    hashmap.pop(letter)
        if(len(hashmap.keys()) > 0):
            return False
        return True