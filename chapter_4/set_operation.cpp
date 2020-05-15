#include <iostream>
using namespace std;

int main() {
    int testCase;
    cin >> testCase;
    for(int i=0; i<testCase; i++) {
        int num;
        int arr1, arr2;
        int interCount=0; int unionCount=0; int differCount=0;
        unsigned int tempArr1[132] = {0,};
        unsigned int tempArr2[132] = {0,};
        unsigned int inter[132] = {0,};
        unsigned int Union[132] = {0,};
        unsigned int differ[132] = {0,};

        cin >> arr1;
        for(int i=0; i<arr1; ++i) {
            cin >> num;
            ++tempArr1[num];
        }
        cin >> arr2;
        for(int j=0; j<arr2; j++) {
            cin >> num;
            ++tempArr2[num];
        }

        for(int i=0; i<132; i++) {
            if(tempArr1[i] && tempArr2[i]) {
                ++inter[i];
                ++interCount;
            }
            if(tempArr1[i] || tempArr2[i]) {
                ++Union[i];
                ++unionCount;
            }
            if(tempArr1[i] && !tempArr2[i]) {
                ++differ[i];
                ++differCount;
            }
        }
        cout << interCount << " ";
        for(int i=0; i<132; ++i) {
            if(inter[i] !=0) cout << i << " ";
        }
        cout << '\n' << unionCount << " ";
        for(int i=0; i<132; ++i) {
            if(Union[i] != 0) cout << i << " ";
        }
        cout << '\n' << differCount << " ";
        for(int i=0; i<132; ++i) {
            if(differ[i] !=0) cout << i << " ";
        }
        cout << '\n';
    }
return 0;
}