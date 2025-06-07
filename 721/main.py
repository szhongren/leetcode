from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        approach
        union find emails, and map email roots to names
        """
        parent_of = {}
        email_to_name = {}

        def get_parent(email: str):
            if parent_of[email] == email:
                return email
            parent = get_parent(parent_of[email])
            parent_of[email] = parent
            return parent_of[email]

        def union(email_a: str, email_b: str):
            parent_a, parent_b = get_parent(email_a), get_parent(email_b)
            parent_of[parent_b] = parent_a

        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                if email not in parent_of:
                    parent_of[email] = email
                    email_to_name[email] = name

        for account in accounts:
            email_1 = account[1]
            for email in account[2:]:
                union(email_1, email)

        results = {}
        for email in parent_of.keys():
            parent = get_parent(email)
            if parent not in results:
                results[parent] = []
            results[parent].append(email)
        result = []
        for parent in results.keys():
            result.append([email_to_name[parent]] + sorted(results[parent]))
        return result
