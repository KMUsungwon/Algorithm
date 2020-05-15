#include <iostream>
#include <cmath>
using namespace std;
int result(int& a,int& b, int& c) {
    if(a+b == c) return 1;
    else if(a+b <c) return 2;
    else return 3;
}

int main() {
    int testCase;
    cin >> testCase;
    int a1,a2,b1,b2,c1,c2;
    for(int i=0; i<testCase; i++) {
        cin >> a1 >> a2 >> b1 >> b2 >> c1 >> c2;
        int lenA, lenB, lenC;

        lenA = pow(b1-a1,2) + pow(b2-a2,2);
        lenB = pow(c1-a1,2) + pow(c2-a2,2);
        lenC = pow(b1-c1,2) + pow(b2-c2,2);

        if(((b2-a2)*(c1-b1))==((b1-a1)*(c2-b2))) {
            cout << 0 << '\n';
        }
        else {
            if(lenA >= lenB && lenA >= lenC) {
              cout << result(lenB,lenC,lenA) << '\n';
            }
            else if(lenB >= lenA && lenB >= lenC) {
                cout << result(lenA, lenC, lenB) << '\n';
            }
            else {
                cout << result(lenA,lenB,lenC) << '\n';
            }
        }
    }
    return 0;
}