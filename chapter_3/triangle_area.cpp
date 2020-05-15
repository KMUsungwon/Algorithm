#include <iostream>
using namespace std;

int main() {
    int testCase;
    cin >> testCase;
    for (int i = 0; i < testCase; i++) {
        int a1, a2, b1, b2, c1, c2;
        int SignedArea;
        cin >> a1 >> a2 >> b1 >> b2 >> c1 >> c2;
        SignedArea = ((b1 - a1) * (c2 - a2) - (c1 - a1) * (b2 - a2));
        if (SignedArea > 0) {
            cout << SignedArea << " 1" << '\n';
        } else if (SignedArea < 0) {
            cout << -SignedArea << " -1" << '\n';
        } else {
            cout << 0 << " 0" << '\n';
        }
    }
return 0;
}