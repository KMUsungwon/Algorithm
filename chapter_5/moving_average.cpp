#include <iostream>
using namespace std;

int main() {
    int testCase;
    cin >> testCase;
    for(int i=0; i<testCase; ++i) {
        int num;
        cin >> num;
        int arr[num];
        for(int j=0; j<num; ++j) {
            cin >> arr[j];
        }
        int zoogi; cin >> zoogi;
        int result = 0;
        cout << num-zoogi+1 << " ";
        for(int k=0; k<num-zoogi+1; ++k) {
            for(int j=0; j<zoogi; ++j) {
                result += arr[k+j];
            }
            cout << result/zoogi << " ";
            result = 0;
        }
        cout << '\n';
    }
    return 0;
}