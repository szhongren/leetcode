from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        approach
        union find
        roots of emails
        email to person
        """
        parent_of = {}
        email_to_person = {}

        def get_parent(email: str):
            if parent_of[email] == email:
                return email
            parent_of[email] = get_parent(parent_of[email])
            return parent_of[email]

        def union(email_a: str, email_b: str):
            parent_a, parent_b = get_parent(email_a), get_parent(email_b)
            if parent_a == parent_b:
                return
            parent_of[parent_b] = parent_a

        # init
        for account in accounts:
            person = account[0]
            for email in account[1:]:
                if email not in parent_of:
                    parent_of[email] = email
                    email_to_person[email] = person

        # union every email for each person
        for account in accounts:
            person = account[0]
            first_email = account[1]
            for email in account[2:]:
                union(email, first_email)

        # for every email in parent_of
        # get its root, that's the key for our result builder
        results_map = {}
        for email in parent_of.keys():
            parent = get_parent(email)
            if parent not in results_map:
                results_map[parent] = []
            results_map[parent].append(email)
        result = []
        for parent in results_map.keys():
            result.append([email_to_person[parent]] + sorted(results_map[parent]))
        return result
