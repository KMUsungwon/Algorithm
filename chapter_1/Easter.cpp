#include <iostream>
using namespace std;

int main() {
	int testCase;
	cin >> testCase;

	for (int temp = 0; temp < testCase; temp++) {
		int year, c, n, t, i, j, k, l, p, q, mon, day;

		cin >> year;
		c = year / 100;
		n = year - (year / 19*19);
		t = (c - 17) / 25;
		i = c - ((c / 4) + ((c - t) / 3)) +
			(n * 19 + 15);
		j = i-(i / 30 * 30);
		k = j - ((j / 28) * (1 - (j / 28)) * (29 / (j + 1)) * ((21 - n) / 11));
		l = (year + (year / 4)) + (j + 2) - c + (c / 4);
		p = l - (l / 7 * 7);
		q = k - p;
		mon = ((q + 40) / 44) + 3;
		day = (q + 28) - (mon / 4 * 31);

		cout << mon << " " << day << endl;
	}
}