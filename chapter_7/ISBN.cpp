#include <iostream>
#include <cstring>
using namespace std;

int main() {
    int testCase; cin >> testCase;
    for(int i=0; i<testCase; i++) {
        char arr[129] = {0,};
        int temp[9] = {0,}, tmp = 0;
        int barCount = 0;
        int flag = 0;
        int arrLoop = 0;
        int numCount = 0, totalCount = 0;
        int sum = 0, check = 0;
        cin >> arr;

        if(strlen(arr) != 13) {
            cout << "0" << '\n';
            continue;
        }

        for(int j=0; j<13; j++) {
            if(arr[j] == '-') barCount++;
        }

        if(barCount != 3) {
            cout << "0" << '\n';
            continue;
        }

        if(arr[0] >=48 && arr[0]<=57) {
            while(arr[arrLoop] != '-') {
                if(arr[arrLoop] >=48 && arr[arrLoop]<=57) {
                    numCount++;
                    temp[tmp++] = (int)arr[arrLoop++] - 48;
                }
                else flag = 1;
            }

            totalCount += numCount;
            if(numCount > 5) flag = 1;
            arrLoop++;
            numCount = 0;

            while (arr[arrLoop] != '-') {
				if (arr[arrLoop] >= 48 && arr[arrLoop] <= 57) {
					temp[tmp++] = (int)arr[arrLoop++] - 48;
					numCount++;
				}
				else flag = 1;
			}
            totalCount += numCount;
            if(numCount > 7 || numCount==0) flag = 1;
            arrLoop++;
            numCount = 0;

            while(arr[arrLoop] != '-') {
                if(arr[arrLoop] >= 48 && arr[arrLoop] <=57) {
                    temp[tmp++] = (int)arr[arrLoop++] - 48;
                    numCount++;
                }
                else flag = 1;
            }
            totalCount += numCount;
            if(numCount > 6 || numCount == 0) flag = 1;
            arrLoop++;

            if(arr[arrLoop] >=48 && arr[arrLoop]<=57 || arr[arrLoop] == 88) totalCount++;

            if(totalCount != 10) flag = 1;
            for(int k=0; k<9; ++k) {
                sum += temp[k] * (10-k);
            }

            while(sum%11 != 0) {
                check++;
                sum++;
            }

            if(check < 10) {
                if(check != ((int)arr[arrLoop])-48) flag = 1;
            }
            else if(check == 10) {
                if(arr[arrLoop] != 'X') flag = 1;
            }
        }
        else flag = 1;

        if(flag) cout << "0" << '\n';
        else cout << "1" << '\n';
        
    }
    return 0;
}