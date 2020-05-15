#include <iostream>
using namespace std;

int main()  {
    int numCase;
    cin >> numCase;

    for(int i=0; i<numCase; i++) {
        int num;
        cin >> num;

        for(int i=0; i<num/2; i++) {
            for(int j=0; j<num; j++) {
                if(((i+j)%2 == 0) && ( num <= num-i+j) && ((i+j) <= num))
                    cout <<"*";
                else if(( num < num-i+j) && ((i+j) < num) )
                    cout <<"+";
                else
                    cout << "-";
            }
            cout << '\n';
        }

        for(int i=0; i<num; i++)  {
            if(i == num/2)
                cout << "*";
            else
                cout << "-";
        }
        cout << '\n';

        for(int i=num/2+1; i<num; i++)  {
            for(int j=0; j<num; j++)  {
                if(((i+j)%2 == 0) && (i+j>=num-1) && (num-j+i>=num))
                    cout << "*";
                else if((i+j>num-1) && (num-j+i>num))
                    cout << "+";
                else
                    cout << "-";
            }
            cout << '\n';
        }
    }
    return 0;
}
