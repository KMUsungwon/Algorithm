#include <iostream>
using namespace std;
void result(int n) {
    int num_1 = 0, num = n;
    while(num){
        if(num%2 == 1) num_1++;
        num/=2;
    }
    if(num_1%2 == 1) cout << n + 2147483648 << '\n';
    else cout << n << '\n';
}
int main() {
    int testCase, number;
    cin >> testCase;
    for(int i=0; i<testCase; i++){
        cin >> number;
        result(number);
    }
    return 0;
}