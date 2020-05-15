#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int testCase;
    cin >> testCase;
    for(int i=0; i<testCase; i++) {
        int n; cin >> n; bool isPrimeNumber=true;
        int end = (int)sqrt(n);
        for(int i=2; i<=end; i++){
            if(n%i==0) {
                isPrimeNumber = false;
                break;
            }
            else isPrimeNumber = true;
        }
        if(isPrimeNumber) cout << 1 << '\n';
        else cout << 0 << '\n';
    }
return 0;
}