#include <iostream>

using namespace std;

class Solution {
public:
    int numberOfSteps(int num) {
        return numberOfStepsRecursive(num, 0);
    }

    int numberOfStepsRecursive(int num, int currentSteps) {
        if (num == 0) {
            return currentSteps;
        }

        if (num % 2 == 1) {
            return numberOfStepsRecursive(num - 1, currentSteps + 1);
        } else {
            return numberOfStepsRecursive(num / 2, currentSteps + 1);
        }
    }
};

int main() {
    Solution solution;
    cout << solution.numberOfSteps(14) << endl;
    cout << solution.numberOfSteps(8) << endl;
}
