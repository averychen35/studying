class MedianFinder:

    def __init__(self):
        # small: maxheap (negative). large: minheap (positive)
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        # may need to rebalance both heaps based on the length
        if not self.small:
            heapq.heappush(self.small, -num)
            return
        small_max = -self.small[0]
        large_min = self.large[0] if self.large else float('inf')

        if num < small_max:
            heapq.heappush(self.small, -num)
            if len(self.small) > len(self.large) + 1:
                heapq.heappush(self.large, -heapq.heappop(self.small))
        elif num > large_min:
            heapq.heappush(self.large, num)
            if len(self.large) > len(self.small) + 1:
                heapq.heappush(self.small, -heapq.heappop(self.large))
        else:
            if len(self.small) <= len(self.large):
                heapq.heappush(self.small, -num)
            else:
                heapq.heappush(self.large, num)
        

    def findMedian(self) -> float:
        # compare lengths of the two halves
        # if equal take the avg of the largest in min heap and smallest in max heap
        if len(self.small) < len(self.large):
            return self.large[0]
        elif len(self.large) < len(self.small):
            return -self.small[0]
        else:
            return (-self.small[0]+self.large[0]) / 2

        
        