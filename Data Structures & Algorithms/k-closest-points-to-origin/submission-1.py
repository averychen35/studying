class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return (point[0]**2 + point[1] **2, point)
        distances = [distance(point) for point in points]
        heapq.heapify(distances)
        closest = []
        for _ in range(k):
            closest.append(heapq.heappop(distances)[1])
        return closest

        