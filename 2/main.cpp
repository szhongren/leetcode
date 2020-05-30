#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

int main();
ListNode* createLinkedListFromVector(vector<int> values);

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return this->addTwoNumbersRecursive(l1, l2, 0);
    }

    ListNode* addTwoNumbersRecursive(ListNode* l1, ListNode* l2, int carry) {
        if (l1 == nullptr && l2 == nullptr) {
            if (carry == 0) {
                return nullptr;
            } else {
                return new ListNode(carry);
            }
        } else if (l1 == nullptr) {
            int currentSum = l2->val + carry;
            int currentDigit = currentSum % 10;
            int newCarry = currentSum / 10;
            return new ListNode(currentDigit, this->addTwoNumbersRecursive(nullptr, l2->next, newCarry));
        } else if (l2 == nullptr) {
            int currentSum = l1->val + carry;
            int currentDigit = currentSum % 10;
            int newCarry = currentSum / 10;
            return new ListNode(currentDigit, this->addTwoNumbersRecursive(l1->next, nullptr, newCarry));
        } else {
            int currentSum = l1->val + l2->val + carry;
            int currentDigit = currentSum % 10;
            int newCarry = currentSum / 10;
            return new ListNode(currentDigit, this->addTwoNumbersRecursive(l1->next, l2->next, newCarry));
        }
    }
};

int main() {
    Solution solution;
    vector<int> firstValue = {2, 4, 3};
    vector<int> secondValue = {5, 6, 4};
    ListNode *answer = solution.addTwoNumbers(createLinkedListFromVector(firstValue), createLinkedListFromVector(secondValue));
    vector<int> thirdValue = {8};
    vector<int> fourthValue = {9, 9};
    ListNode *answer2 = solution.addTwoNumbers(createLinkedListFromVector(thirdValue), createLinkedListFromVector(fourthValue));
    return 0;
}

ListNode* createLinkedListFromVector(vector<int> values) {
    vector<ListNode*> nodes = {};
    for (auto const& value: values) {
        nodes.push_back(new ListNode(value));
    }
    for (int i = 0; i < nodes.size() - 1; i++) {
        nodes.at(i)->next = nodes.at(i + 1);
    }
    return nodes.at(0);
}
