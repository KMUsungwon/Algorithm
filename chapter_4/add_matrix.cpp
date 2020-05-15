#include <iostream>
using namespace std;

int main() {
    int testCase;
    cin >> testCase;
    for (int i = 0; i < testCase; ++i) {
        int row, col;
        cin >> row >> col;
        int arr1[row][col]; int arr2[row][col]; int result[row][col];

        for(int i=0; i<row; ++i) {
            for(int j=0; j<col; ++j) {
                cin >> arr1[i][j];
            }
        }
        for(int i=0; i<row; ++i) {
            for(int j=0; j<col; ++j) {
                cin >> arr2[i][j];
            }
        }

        for(int i=0; i<row; ++i) {
            for(int j=0; j<col; ++j) {
                result[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        for(int i=0; i<row; ++i) {
            for(int j=0; j<col; ++j) {
                cout << result[i][j] << " ";
            }
            cout << '\n';
        }

        
    }
    return 0;
}