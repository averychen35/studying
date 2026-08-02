class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        str1, str2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            str1[ord(s1[i])-ord('a')] += 1
            str2[ord(s2[i])-ord('a')] += 1
        
        matches = 0
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            idx = ord(s2[r]) - ord('a')
            str2[idx] += 1
            # adding right adds a new match
            if str1[idx] == str2[idx]:
                matches += 1
            # adding right removes a new match
            elif str1[idx] + 1 == str2[idx]:
                matches -= 1
            
            idx = ord(s2[l]) - ord('a')
            # removing left adds a new match
            str2[idx] -= 1
            if str1[idx] == str2[idx]:
                matches += 1
            # removing left removes a match
            if str1[idx] == str2[idx] + 1:
                matches -= 1
            l += 1
        return matches == 26

        


        
        