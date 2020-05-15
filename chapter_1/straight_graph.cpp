#include <iostream>
using namespace std;

int main() {
    int testCase;
    cin >> testCase;
    for (int k = 0; k < testCase; k++) {
        int lineNum;
        cin >> lineNum;
        int starPoint = lineNum - 1;

        for (int i = 0; i < lineNum; i++) {
            if (i == lineNum / 2) {
                for (int temp = 0; temp < lineNum; temp++) {
                    if (temp == lineNum / 2) cout << 'O';
                    else cout << '+';
                }
            } else {
                for (int j = 0; j < lineNum; j++) {
                    if (j == starPoint) {
                        cout << '*';
                    } else if (j == lineNum / 2) {
                        cout << 'I';
                    }  else {
                        cout << '.';
                    }
                }
            }
            starPoint--;
            cout << '\n';
        }
    }
    return 0;
}