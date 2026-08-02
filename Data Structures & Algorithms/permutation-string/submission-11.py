class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check length of s1 and s2
        if len(s1) > len(s2):
            return False
        # populate the counts and matches
        matches = 0
        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        if matches == 26:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            r_idx = ord(s2[r]) - ord('a')
            s2Count[r_idx] += 1
            if s2Count[r_idx] == s1Count[r_idx]:
                matches += 1
            if s2Count[r_idx] == s1Count[r_idx] + 1:
                matches -= 1

            l_idx = ord(s2[l]) - ord('a')
            s2Count[l_idx] -= 1
            if s2Count[l_idx] == s1Count[l_idx]:
                matches += 1
            if s2Count[l_idx] + 1 == s1Count[l_idx]:
                matches -= 1
            if matches == 26:
                return True
            l += 1
        return matches == 26
        

        


        
        