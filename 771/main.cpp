#include <iostream>
#include <set>

using namespace std;

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        set<char> uniqueJewels (J.begin(), J.end());
        int result = 0;
        for (const auto& stone: S) {
            if (uniqueJewels.find(stone) != uniqueJewels.end()) {
                result += 1;
            }
        }
        return result;
    }
};

int main() {
    Solution solution;
    cout << solution.numJewelsInStones("aA", "aAAbbbb") << endl;
    cout << solution.numJewelsInStones("z", "ZZ") << endl;
}
