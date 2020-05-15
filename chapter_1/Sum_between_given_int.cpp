#include <iostream>
using namespace std;

int main() {
	int TestCase;
	cin >> TestCase;


	for (int i=0; i < TestCase; i++) {
		int A = 0;
		int B = 0;
		int sum = 0;
		cin >> A >> B;
		sum = A;
		for (int j=A + 1; j <= B; j++) {
			sum += j;
		}
		cout << sum << endl;
	}
}