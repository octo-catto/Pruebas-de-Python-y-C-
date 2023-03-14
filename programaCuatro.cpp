#include<stdio.h>
#include<time.h>
#include<iostream>
#include<limits>
using namespace std;

int main()
{
    clock_t T;
    unsigned int i;
    unsigned long A = 2000;
    unsigned long B = 1000;
    unsigned long C = 100;
    T = clock();
    for (i = A - 1; i > 0; i--)
    {
        A *= i;
    }
    for (i = B - 1; i > 0; i--)
    {
        B *= i;
    }
    for (i = C - 1; i > 0; i--)
    {
        C *= i;
    }
    T = clock() - T;
    printf("El programa cuatro se ejecutó en: %.3f segundos. \n", (float)T/CLOCKS_PER_SEC);
    return 0;
}
