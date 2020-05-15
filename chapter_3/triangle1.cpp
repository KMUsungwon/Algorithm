#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int testCase;
    int a; int b; int c;
    cin >> testCase;
    for(int i=0; i<testCase; i++) {
        cin >> a >> b >> c;

        if(a+b <= c) {
            cout << 0 << '\n';
        }
        else {
        if((pow(a,2)+pow(b,2) == pow(c,2))) {
            cout << 2 << '\n';
        }
        else if((a==b&&b!=c) || (a!=c&&b==c) || (b!=c&&a==c)) {
            cout << 3 << '\n';
        }
        else if(a==b && b==c) {
            cout << 1 << '\n';
        }
        else {
            cout << 4 << '\n';
        }
        }
    }
    return 0;
}