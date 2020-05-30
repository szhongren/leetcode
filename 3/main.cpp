#include <iostream>
#include <map>
#include <set>
#include <string>

using namespace std;

int main();

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int> seenAtIndex ({});
        for (int i = 0; i < s.size(); i++) {
            cout << s[i] << endl;
        }
        return 0;
    }
};


int main() {
    Solution solution;
    cout << solution.lengthOfLongestSubstring("abcabcbb") << endl;
    cout << solution.lengthOfLongestSubstring("bbbbb") << endl;
    cout << solution.lengthOfLongestSubstring("pwwkew") << endl;
}
