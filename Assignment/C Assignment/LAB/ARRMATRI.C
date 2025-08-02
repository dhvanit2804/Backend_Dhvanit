#include<stdio.h>
#include<conio.h>

void main()
{
	int arr1D[5],i,j;
	int arr2D[3][3], sum=0;
	clrscr();
	//1D Array
	printf("\nEnter 5 integer for 1D Array : ");
	for(i=0;i<5;i++)
	{
		printf("\nElement %d: ",i+1);
		scanf("%d",&arr1D[i]);
	}
	printf("\n1D Array Elements :\n");
	for(i=0;i<5;i++)
	{
		printf("\n%d",arr1D[i]);
	}
	//2D Array
	printf("\nEnter elements for 3*3 matrix:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\nElements[%d][%d]: ",i,j);
			scanf("%d",&arr2D[i][j]);
			sum+=arr2D[i][j];
		}
	}
	printf("\n3*3 Matrix:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t%d",arr2D[i][j]);
		}
		printf("\n");
	}
	printf("\nSum of all elements in matrix = %d",sum);
	getch();
}