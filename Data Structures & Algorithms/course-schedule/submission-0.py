class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for i in prerequisites:
            graph[i[0]].append(i[1])

        path = set()
        def dfs(course):
            if course in path:
                return False
            if graph[course] == []:
                return True
            
            path.add(course)
            for i in graph[course]:
                if not dfs(i):
                    return False
            path.remove(course)
            graph[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True