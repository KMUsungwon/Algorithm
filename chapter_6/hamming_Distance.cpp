#include <iostream>
using namespace std;

int main() {
    int testCase; cin >> testCase;
    for(int i=0; i<testCase; ++i) {
        int hamming_distance = 0; int weight_A=0; int weight_B=0;
        int a, b; cin >> a >> b;
        int binA[32];int binB[32];

        for(int j=0;  j<32; ++j) {
            binA[j] = a%2;
            binB[j] = b%2;
            a = a/2; b = b/2;
            if(binA[j] == 1) ++weight_A;
            if(binB[j]) ++weight_B;
            if(binA[j] != binB[j]) ++hamming_distance;
        }

        cout << weight_A << " " << weight_B << " " << hamming_distance <<'\n';
    }
    return 0;
}