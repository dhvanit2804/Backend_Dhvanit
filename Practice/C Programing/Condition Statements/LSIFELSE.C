#include<stdio.h>
#include<conio.h>

int main()
{
	int a,b,c;
	int largest,smallest;
	printf("\nEnter A : ");
	scanf("%d",&a);
	printf("\nEnter B : ");
	scanf("%d",&b);
	printf("\nEnter C : ");
	scanf("%d",&c);
	//Largest
	if(a>=b && a>=c)
		largest = a;
	else if(b>=a && b>=c)
		largest = b;
	else
		largest = c;
	printf("\nLargest = %d",largest);
	//Smallest
	if(a<=b && a<=c)
	{
		smallest = a;
		printf("\nSmallest = %d",smallest);
	}
	else if(b<=a && b<=c)
	{
		smallest = b;
		printf("\nSmallest = %d",smallest);
	}
	else
	{
		smallest = c;
		printf("\nSmallest = %d",smallest);
	}
	return 0;
	getch();
}
