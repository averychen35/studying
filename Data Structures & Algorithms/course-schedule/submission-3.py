class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cycle detection problem
        # construct graph
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dest in prerequisites:
            indegree[dest] += 1
            adj[src].append(dest)
        # detect cycles (kahn's)
        # find ones with indegree 0
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        goal = 0
        while q:
            node = q.popleft()
            goal += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return goal == numCourses




        # something already in our seen set
        