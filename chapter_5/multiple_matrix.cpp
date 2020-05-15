#include <iostream>
using namespace std;

int main() {
    int testCase; cin >> testCase;

    for(int i=0; i<testCase; ++i) {
        int r,s,t;
        int sum;
        cin >> r >> s >> t;
        int Arr1[r][s]; int Arr2[s][t]; int resultArr[r][t];
        for(int j=0; j<r; ++j) {
            for (int k=0; k<s; ++k) {
                cin >> Arr1[j][k];
            }
        }


        for(int tmp=0; tmp<s; ++tmp) {
            for(int kk=0; kk<t; ++kk) {
                cin >> Arr2[tmp][kk];
            }
        }


        for(int i=0; i<r; ++i) {
            for(int j=0; j<t; ++j) {
                sum = 0;
                for(int k=0; k<s; ++k) {
                    sum += Arr1[i][k] * Arr2[k][j];
                }
                resultArr[i][j] = sum;
            }
        }

        for(int i=0; i<r; ++i) {
            for(int j=0; j<t; ++j) {
                cout << resultArr[i][j] << " ";
            }
            cout << '\n';
        }
    }

    return 0;
}