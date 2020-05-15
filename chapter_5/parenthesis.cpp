#include <iostream>
#include <stack>
using namespace std;
bool check(string str) {
    stack<char> st;
    for(int j=0; j<str.length(); ++j) {
        if(str[j] == '(' || str[j] == '[' || str[j] == '{') st.push(str[j]);
        else {
            if(st.empty()) {
                return false;
            }
            if(str[j] == ']' && st.top()== '[') st.pop();
            else if(str[j] == ')' && st.top()== '(') st.pop();
            else if(str[j] == '}' && st.top()== '{') st.pop();
            else st.push(str[j]);
        }
    }
    return st.empty();
}

int main() {
    int testCase; cin >> testCase;
    for(int i=0; i<testCase; ++i) {
        string str;
        cin >> str;
        if(check(str)) cout << "1" << '\n';
        else cout << "0" << '\n';
    }
    return 0;
}