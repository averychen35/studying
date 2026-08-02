class Solution:

    def encode(self, strs: List[str]) -> str:
        # length of string then #
        res = []
        for curr_str in strs:
            res.append(str(len(curr_str)))
            res.append('#')
            res.append(curr_str)
        return "".join(res)



    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i: j])
            i = j
        return res
            
            
            
