#include<stdio.h>
#include<time.h>
#include<iostream>
#include<limits>
using namespace std;

int main()
{
    clock_t T;
    unsigned int i;
    unsigned long A = 50;
    for (i = A - 1; i > 0; i--)
    {
        A *= i;
    }
    cout << numeric_limits<unsigned long long int>::max() << endl;
    cout << numeric_limits<unsigned long int>::max() << endl;
    cout << numeric_limits<unsigned int>::max() << endl;
    return 0;
}
