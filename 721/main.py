from typing import List
from pprint import pprint


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        roots = {}
        emails_to_person = {}

        def find(email: str) -> str:
            if roots[email] != email:
                roots[email] = find(roots[email])
            return roots[email]

        def union(email1: str, email2: str):
            root1 = find(email1)
            root2 = find(email2)
            if root1 == root2:
                return
            roots[root2] = root1

        # First pass: Initialize each email's root and person mapping
        for account in accounts:
            person = account[0]
            for email in account[1:]:
                if email not in roots:
                    roots[email] = email
                    emails_to_person[email] = person

        # Second pass: Union emails within each account
        for account in accounts:
            for email in account[2:]:  # Start from second email
                union(account[1], email)  # Union with first email

        # Group emails by root
        results = {}
        for email in roots:
            root = find(email)  # Important: use find() here
            if root not in results:
                results[root] = []
            results[root].append(email)

        return [
            [emails_to_person[root]] + sorted(emails)
            for root, emails in results.items()
        ]


sol = Solution()
print(
    sol.accountsMerge(
        [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
    )
)

print(
    sol.accountsMerge(
        [
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
        ]
    )
)
