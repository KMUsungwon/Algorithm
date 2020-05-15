#include<iostream>
using namespace std;

int main() {

    int testCase;
    cin >> testCase;

    while(testCase != 0)
    {
        int k;
        cin >> k;
        for (int i = 1;i <= k;i++)
        {
            int num = i;
            for (int j = 1;j <= i;j++) {
                cout << num << " ";
                num += (k - j);
            }
            cout << "\n";

        }
        testCase--;
    }
}
