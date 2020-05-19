#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

int main() {

int testCase; cin >> testCase;
for(int i=0; i<testCase; i++) {
    int bytes[4];
    unsigned int n;
    int type;
    cin >> type;
    if( type == 1) {
        unsigned int sum = 0;
        int a,b,c,d;
        char dot;
        cin >> a >> dot >> b >> dot >> c >> dot >> d;
        sum = a*(pow(256,3)) + b*(pow(256,2)) + c*(pow(256,1)) + d*(pow(256,0));
        cout << sum << '\n';        
        }
    else if(type ==2) {
        int bits = 0;
        cin >> n;
        for(int i=0; i<=3; i++) {
            bytes[i] = (n >> bits) & 0xFF;
            bits += 8;
            }
            cout << bytes[3] << '.' << bytes[2] << '.' << bytes[1] << '.' << bytes[0] << '\n';
        }    
    }
    return 0;  
}

