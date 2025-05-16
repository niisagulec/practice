
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)

        # Dersleri grafa yerleştiriyoruz
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = set()  # Daha önce kontrol ettiğimiz dersler
        path = set()     # Şu anki DFS yolundaki dersler (döngü kontrolü)

        def dfs(course):
            if course in path:
                return False  # Aynı DFS yolunda aynı kursa tekrar geldik → döngü
            if course in visited:
                return True   # Daha önce kontrol edildi → sıkıntı yok

            path.add(course)  # DFS zincirine eklendi

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            path.remove(course)      # DFS zincirinden çıkıyoruz
            visited.add(course)      # Artık bu kurs kontrol edildi
            return True

        # Tüm kurslar için DFS başlat
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
    
    
# Test 1
numCourses = 2
prerequisites = [[1, 0]]
print(Solution().canFinish(numCourses, prerequisites))  

# Test 2
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(Solution().canFinish(numCourses, prerequisites))  

# Test 3
numCourses = 4
prerequisites = [[1,0],[2,1],[3,2]]
print(Solution().canFinish(numCourses, prerequisites))  

# Test 4
numCourses = 3
prerequisites = [[0,1],[1,2],[2,0]]
print(Solution().canFinish(numCourses, prerequisites))  
