# User function Template for python3

from collections import defaultdict

class FindUnion:
    def __init__(self, N):
        self.parents = list(range(N))
        
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
        
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

class Solution:
    def accountsMerge(self, accounts):
        # Code here
        findUnion = FindUnion(len(accounts))
        
        mailOwnership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in mailOwnership:
                    findUnion.union(i, mailOwnership[email])
                mailOwnership[email] = i
        
        result = defaultdict(list)
        for email, owner in mailOwnership.items():
            result[findUnion.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in result.items()]
