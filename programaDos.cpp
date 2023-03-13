#include<stdio.h>
#include<time.h>

int main()
{
    clock_t T;
    int i, A = 0;
    T = clock();
    for (int i = 0; i < 1000000000; i++)
    {
        printf("%d \n", A);
        A = 3*A;
    }
    T = clock() - T;
    printf("El programa dos se ejecutó en: %f segundos. \n", (float)T/CLOCKS_PER_SEC);
    return 0;
}

