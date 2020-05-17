#include <iostream>
#include <cmath>
using namespace std;

void hamming(int data);
void realdata(int data);
void paritybit(int arr[]);
void checkparity(int arr[]);

int main() {
    int testCase; cin >> testCase;
    for(int i=0; i<testCase; ++i) {
        int n, num;
        cin >> n >> num;

        if(n==0) hamming(num);
        else if(n==1) realdata(num);
    }
    return 0;
}

void hamming(int data) {
    int Arr[33] = {0,};
    int i=1;

    while(data >0) {
        if(i==1 || i==2 || i==4 || i==8 || i==16 || i==32) i++;
        else {
            Arr[i++] = data%2;
            data /= 2;
        }
    }

    paritybit(Arr);

    int result = 0;
    for(int i=1; i<33; ++i) {
        result += Arr[i]*pow(2,i-1);
    }
    cout << result << '\n';
}

void paritybit(int arr[]) {
    for(int i=1; i<=32; ++i) {
        int count =0; //개수 판별
        if(i==1 || i==2 || i==4 || i==8 || i==16 || i==32) {
            for(int j=i; j<=32; j++) {
                if((j%(i*2)>=i) && (j%(i*2)<=i*2-1)) {
                    if(arr[j] == 1) ++count;
                }
            }
            if(count%2 != 0) arr[i] = 1;
        }
    }
}

void realdata(int data) {
    int Arr[33] = {0,};
    int real[27] = {0,};
    int i=1;
    while(data >0) {
        Arr[i++] = data%2;
        data /= 2;
    }

    checkparity(Arr);

    int j=1;
    for(int i=1; i<=32; ++i) {
        if(i==1 || i==2 || i==4 || i==8 || i==16 || i==32) continue;
        else {
            real[j++] = Arr[i];
        }
    }

    int result = 0;
    for(int i=1; i<27; ++i) {
        result += real[i]*pow(2,i-1);
    } 
    cout << result << '\n';
}

void checkparity(int arr[]) {
    int error = 0;
    for(int i=1; i<=32; ++i) {
        int count = 0;
        if(i==1 || i==2 || i==4 || i==8 || i==16 || i==32) {
            for(int j=i; j<=32; ++j) {
                if((j%(i*2)>=i) && j%(i*2)<=i*2-1 && (arr[j]==1)) {
                    ++count;
                }
            }
            if(count%2 != 0) error+=i;
        }
    }
    if(arr[error]==1) arr[error] = 0;
    else if(arr[error]==0) arr[error] = 1;
}