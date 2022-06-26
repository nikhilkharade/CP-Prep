class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visited = {}
        for i in s:
            
            if visited.get(i):
                visited[i] += 1
            else:
                visited[i] = 1
        
        
        if len(s) == len(t):
            for i in t:
                if visited.get(i):
                    visited[i] -= 1
            return not bool(sum(visited.values()))
        
        return False
        
        
        
        