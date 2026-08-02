class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        max_prefix = 0
        suffix = [0] * len(height)
        max_suffix = 0
        total = 0

        for i in range(len(height)):
            prefix[i] = max_prefix
            if height[i] > max_prefix:
                max_prefix = height[i]
        for i in range(len(height) - 1, -1, -1):
            suffix[i] = max_suffix
            if height[i] > max_suffix:
                max_suffix = height[i]
        print(prefix)
        print(suffix)
        
        for i in range(len(height)):
            additional = min(prefix[i], suffix[i]) - height[i]
            print(additional)
            if additional > 0:
                total += additional
        return total



        