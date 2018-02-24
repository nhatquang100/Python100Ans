"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        d = {e.id: e for e in employees}
        
        ans = 0
        stack = [d[id]]
        while stack:
            e = stack.pop()
            ans += e.importance
            stack += [d[id] for id in e.subordinates]
        return ans