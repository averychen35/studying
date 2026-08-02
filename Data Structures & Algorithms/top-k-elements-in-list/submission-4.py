class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count up elements
        # put them in a max heap
        # delete k elements from max heap
        vals = {}
        for num in nums:
            if num not in vals:
                vals[num] = 0
            vals[num] += 1
        
        heap = []
        for num in vals.keys():
            heapq.heappush(heap, (vals[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [val[1] for val in heap]
        