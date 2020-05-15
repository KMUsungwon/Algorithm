#include <iostream>

using namespace std;
int convertSec(int H, int M, int S) {
    return S+(M*60)+(H*60*60);
}

int main() {
    int testCase;
    cin >> testCase;

    int perNum;
    for (int i = 0; i < testCase; i++) {
        cin >> perNum;
        int H, M, S, h, m, s;
        int days, hours, minutes, seconds;
        int total=0;

        for (int j = 0; j < perNum; j++) {
            cin >> H >> M >> S >> h >> m >> s;
            total += convertSec(h, m, s) - convertSec(H, M, S);
        }
        seconds = total%60;
        minutes = total/60;
        hours = minutes/60;
        minutes = minutes%60;
        days = hours/24;
        hours = hours%24;

        cout << days << ' ' << hours << ' ' << minutes << ' ' << seconds << '\n';
    }
    return 0;
}
