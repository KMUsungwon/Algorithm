#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int testCase;
    cin >> testCase;
    for(int i=0; i<testCase; i++) {
        int x1, y1, x2, y2; 
        int px1; int py1; 
        int straight; int rightAngle;
        cin >> x1 >> y1 >> x2 >> y2;
        cin >> px1 >> py1;
        int leftx = x1; int lefty = y2;
        int rightx = x2; int righty = y1;
        if((x1<=px1&&px1<=x2) &&(y1<=py1&&py1<=y2)) {
            straight = 0;
            rightAngle = 0;
        }
        else if(px1<x1 && py1<y1) {
            straight = pow((px1-x1),2) + pow((py1-y1),2);
            rightAngle = abs(px1-x1) + abs(py1-y1);
        }
        else if(px1<x1 && (y1<=py1&&py1<=lefty)) {
            straight = pow((px1-x1),2);
            rightAngle = abs(px1-x1);
        }
        else if(px1<leftx && py1>lefty) {
            straight = pow((px1-leftx),2) + pow((py1-lefty),2);
            rightAngle = abs(px1-leftx) + abs(py1-lefty);
        }
        else if((leftx<=px1&&px1<=x2) && py1>y2) {
            straight = pow((py1-y2),2);
            rightAngle = abs(py1-y2);
        }
        else if(px1>x2 && py1>y2) {
            straight = pow((px1-x2),2) + pow((py1-y2),2);
            rightAngle = abs(px1-x2) + abs(py1-y2);
        }
        else if(px1>x2 && (y1<=py1&&py1<=y2)) {
            straight = pow((px1-x2),2);
            rightAngle = abs(px1-x2);
        }
        else if(px1>x2 && py1<y1) {
            straight = pow((px1-x2),2) + pow((py1-y1),2);
            rightAngle = abs(px1-x2) + abs(py1-y1);
        }
        else if((x1<=px1&&px1<=x2) && py1<y1) {
            straight = pow((py1-y1),2);
            rightAngle = abs(py1-y1);
        }
        cout << straight << " " << rightAngle << '\n';
    }
    return 0;
}