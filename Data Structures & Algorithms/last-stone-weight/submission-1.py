class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-stone for stone in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            first_stone = heapq.heappop(neg_stones)
            second_stone = heapq.heappop(neg_stones)
            if second_stone > first_stone:
                heapq.heappush(neg_stones, first_stone-second_stone)
        return 0 if len(neg_stones) == 0 else -neg_stones[0]
        