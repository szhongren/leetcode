#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string defangIPaddr(string address) {
        vector<string> ipAddressParts = {};
        string currentPart = "";
        for (const char& character: address) {
            if (character == '.') {
                ipAddressParts.push_back(currentPart);
                currentPart = "";
                continue;
            }
            currentPart += character;
        }
        ipAddressParts.push_back(currentPart);
        currentPart = "";
        string result = "";
        for (int i = 0; i < ipAddressParts.size(); i++) {
            result += ipAddressParts[i];
            if (i == ipAddressParts.size() - 1) {
                break;
            }
            result += "[.]";
        }
        return result;
    }
};

int main() {
    Solution solution;
    cout << solution.defangIPaddr("1.1.1.1") << endl;
    cout << solution.defangIPaddr("255.100.50.0") << endl;
}
