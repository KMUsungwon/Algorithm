#include <iostream>
using namespace std;

int main()
{
  int testCase;
  cin >> testCase;
  for(int i=0; i < testCase; i++){
    int numData,data;
    int sum = 0;
    cin >> numData;

    for(int j=0; j < numData; j++)
    {
      cin>>data;
      sum+=data;
    }
    cout << sum << '\n';
  }

  return 0;
}
