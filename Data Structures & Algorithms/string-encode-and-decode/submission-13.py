class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#"+ s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        integer = 0

        while integer < len(s):
            num_end = integer
            while s[num_end] != '#':
                num_end += 1
            length = int(s[integer: num_end])
            res.append(s[num_end+1:num_end + 1 + length])
            integer = num_end + length + 1
        return res


