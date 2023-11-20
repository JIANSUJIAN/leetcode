#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start


from typing import List


    # Approach 1: Depth First Search (DFS)
    # Time: Space:

# class Solution:
    # def __init__(self) -> None:
    #     self.adjacent = {}
    #     self.visited = set()
    
    # def dfs(self, merged_account, email):
    #     self.visited.add(email)

    #     # Add the email to the current component's emails
    #     merged_account.append(email)

    #     if email not in self.adjacent:
    #         return

    #     for neighbor in self.adjacent[email]:
    #         if neighbor not in self.visited:
    #             self.dfs(merged_account, neighbor)
    
    # def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

    #     account_list_size = len(accounts)

    #     # Building the adjacency list
    #     for account in accounts:
    #         account_size = len(account)
    #         # Adding edge bewtween first email to all other emails in the account
    #         account_first_email = account[1]
    #         for j in range(2, account_size):
    #             account_email = account[j]
                
    #             if account_first_email not in self.adjacent:
    #                 self.adjacent[account_first_email] = []
    #             self.adjacent[account_first_email].append(account_email)

    #             if account_email not in self.adjacent:
    #                 self.adjacent[account_email] = []
    #             self.adjacent[account_email].append(account_first_email)
        
    #     # Traverse over all the accounts to store components
    #     merged_accounts = []
    #     for account in accounts:
    #         account_name = account[0]
    #         account_first_email = account[1]

    #         # Perform DFS only if email is not visited yet
    #         if account_first_email not in self.visited:
    #             merged_account = [account_name] # Adding account name at the 0th index
    #             self.dfs(merged_account, account_first_email)
    #             # Sort the account eamils after the first element (the account name)
    #             merged_accounts.append(sorted(merged_account[1:]))
    #             merged_accounts[-1].insert(0, account_name)
        
    #     return merged_accounts

    # Approach 2: Disjoint Set Union (DSU)
    # Time: Space:
class DSU:
        def __init__(self, size):
            self.root= [i for i in range(size)]
        
        def find_root(self, x):
            # Could optimize with path compression
            while x != self.root[x]:
                x = self.root[x]
            return x

        def union(self, x, y):
            rootX = self.find_root(x)
            rootY = self.find_root(y)
            if rootX != rootY:
                self.root[rootX] = rootY
        
        def connected(self, x, y):
            return self.find_root(x) == self.find_root(y)
    
class Solution:
        def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
            account_list_size = len(accounts)
            dsu = DSU(account_list_size)

            # Set the group of the email as the index of current account
            email_group = {}

            for i in range(account_list_size):
                 account_size = len(accounts[i])

                 for j in range(1, account_size):
                    email = accounts[i][j]
                    name = accounts[i][0]

                    if email not in email_group:
                         email_group[email] = i
                    else:
                        dsu.union(i, email_group[email])
            
            # Each email will be added to a map where the key is the email's representative
            components = {}
            for email, group in email_group.items():
                group_rep = dsu.find_root(group)

                if group_rep not in components:
                    components[group_rep] = []
                components[group_rep].append(email)

            merged_accounts = []
            for group, component in components.items():
                component.sort()
                component.insert(0, accounts[group][0])
                merged_accounts.append(component)
            
            return merged_accounts
            
        
        
        
# @lc code=end

