#include <stdio.h>
#include <conio.h>

void main()
{
    int a;
    printf("\nEnter A:");
    scanf("%d", &a);
    if (a % 2 == 0)
    {
        printf("\nA is Even Num");
    }
    else
    {
        printf("\nA is Odd Num");
    }
};