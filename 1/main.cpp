#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main();
void printVector(vector<int> vec);

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result = {};
        map<int, int> seenAtIndex ({});
        for (int i = 0; i < nums.size(); i++) {
            auto iteratorToValue = seenAtIndex.find(target - nums[i]);
            if (iteratorToValue != seenAtIndex.end()) {
                // found
                result.push_back((*iteratorToValue).second);
                result.push_back(i);
                break;
            }
            seenAtIndex.insert({nums[i], i});
        }
        return result;
    }
};

void printVector(vector<int> vec) {
    cout << '{';

    for (auto const& val: vec) {
        cout << val << ", ";
    }

    cout << "}\n";
}

int main() {
    Solution solution;
    vector<int> values = {122, 87, 4, 5};
    printVector(solution.twoSum(values, 9));
}
