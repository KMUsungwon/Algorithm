#include <iostream>
using namespace std;

int main() {
    int testCase;
    cin >> testCase;


    for(int i=0; i<testCase; i++) {
        int numData, data;
        int lastDigit = 1;

        cin >> numData;
        for(int j=0; j<numData; j++) {
            cin >> data;
            lastDigit *= data%10;
            lastDigit %=10;
        }
        cout << lastDigit << '\n';

    }
    return 0;
}