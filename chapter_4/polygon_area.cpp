#include <iostream>
using namespace std;

int main() {
    int testCase; cin >> testCase;
    for(int i=0; i<testCase; i++) {
        int n; cin >> n;
        int xArr[n+1];
        int yArr[n+1];
        for(int j=0; j<n; j++) {
            int x,y; cin >> x >> y;
            xArr[j] = x; yArr[j] = y;
        }
        xArr[n] = xArr[0];
        yArr[n] = yArr[0];
        int a=0,b=0;

        for(int k=0; k<n; k++) {
            a += xArr[k] * yArr[k+1];
            b += xArr[k+1] * yArr[k];
        }
        if(a-b>0) cout << a-b << " 1" << '\n';
        else cout << -(a-b) << " -1" << '\n';
    }
    return 0;
}