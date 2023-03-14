#include<stdio.h>
#include<math.h>
#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    clock_t T;
    int i;
    ofstream archivoTexto ("archivoTexto.txt");
    T = clock();
    for (i = 0; i < 1000; i++)
    {
        archivoTexto.open("archivoTexto.txt", ios::app);
        archivoTexto << i << endl;
        archivoTexto.close();
    }
    T = clock() - T;
    printf("El programa tres se ejecutó en: %.3f segundos. \n", (float)T/CLOCKS_PER_SEC);
    return 0;
}
