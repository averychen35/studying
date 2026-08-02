class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # new interval goes before
                newIntervals.append(newInterval)
                return newIntervals + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # new interval goes after current
                newIntervals.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        newIntervals.append(newInterval)
        return newIntervals
