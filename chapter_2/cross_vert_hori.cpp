#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int testCase;
    cin >> testCase;
    for(int i=0; i<testCase; i++) {
        int x1, y1, x2, y2, x3, y3, x4, y4;
        cin >> x1 >> y1 >> x2 >> y2;
        cin >> x3 >> y3 >> x4 >> y4;
        int temp;
        if (y1 == y2 && x3==x4) {
            swap(x1,x3);
            swap(y1,y3);
            swap(x2,x4);
            swap(y2,y4);
        }
        if(y1 > y2) {
            swap(y2,y1);
        }
        if(x3 > x4) {
            swap(x3,x4);
        }

        if(x1>x3&&x1<x4 && y1<y3&&y3<y2) {
            cout << 1 << '\n';
        }
        else if(y1<=y3 && y3<=y2) {
            if(x1>x4 || x3>x1) cout << 0 << '\n';
            else cout << 2 << '\n';
        }
        else if(x3<=x1 && x1 <=x4) {
            if(y3<y1 || y3>y2) cout << 0 << '\n';
            else cout << 2 << '\n';
        }
        else cout << 0 << '\n';
    }
    return 0;
}