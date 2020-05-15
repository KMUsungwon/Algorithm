#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int max = 398580750;
    int testCase; cin >> testCase;
    for(int i=0; i<testCase; ++i) {
        int count = 0;
        int arr[1350];

        int n; cin >> n;
        for(int c=0; c<=12; ++c) {
            for(int b=0; b<=18; ++b) {
                for(int a=0; a<=29; ++a) {
                    if(pow(2,a) * pow(3,b) * pow(5,c) > max) break;
                    else {
                        arr[count] = (pow(2,a)*pow(3,b)*pow(5,c));
                        ++count;
                    }
                }
            }
        }
        sort(arr, arr+1350);
        cout << arr[n-1] << '\n';
    }
    return 0;
}