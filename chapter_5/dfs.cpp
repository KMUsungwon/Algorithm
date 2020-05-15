#include <iostream>
#include <algorithm>
using namespace std;

int room(char Arr[][101],int x, int y, int cnt) {
    Arr[x][y] = '+';
    ++cnt;
    if(Arr[x][y-1] == '.') {cnt = room(Arr,x,y-1,cnt);}
    if(Arr[x][y+1] == '.') {cnt = room(Arr,x,y+1,cnt);}
    if(Arr[x-1][y] == '.') {cnt = room(Arr,x-1,y,cnt);}
    if(Arr[x+1][y] == '.') {cnt = room(Arr,x+1,y,cnt);}
    return cnt;
}

int main() {
    int testCase; cin >> testCase;
    for(int i=0; i<testCase; ++i) {
        int roomCount[101] = {0,};
        char Arr[101][101];
        int m,n; cin >> m >> n;
        for (int j=0; j<n; ++j) {
            for(int k=0; k<m; ++k) {
                cin >> Arr[j][k];
            }
        }

        int index = 0;
        int sizeOfroom=0;

        for(int j=0; j<n; ++j) {
            for(int k=0; k<m; ++k) {
                if(Arr[j][k] == '.') {
                    sizeOfroom = room(Arr, j, k, sizeOfroom);
                    roomCount[index] = sizeOfroom;
                    ++index;
                    sizeOfroom = 0;
                }
            }
        }
        sort(roomCount, roomCount+index);
        cout << index << '\n';

        for(int tmp=index-1; tmp>=0; --tmp) {
            cout << roomCount[tmp] << " ";
        }
        cout << '\n';
    }
    return 0;
}