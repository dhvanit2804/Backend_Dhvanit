#include<stdio.h>
#include<conio.h>

void main()
{
	int arr[5],i;
	int matrix[3][3],j,sum=0;

	clrscr();

	// 1D Array
	printf("\nEnter 5 integers:\n");
	for (i=0;i<5;i++)
	{
		scanf("%d",&arr[i]);
	}

	printf("\nYou entered (1D Array): ");
	for(i=0;i<5;i++)
	{
		printf("%d",arr[i]);
	}

	// 2D Array
	printf("\n\nEnter 9 integers for 3*3 matrix:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			scanf("%d",&matrix[i][j]);
		}
	}

	printf("\nMatrix (3*3):\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%d\t",matrix[i][j]);
			sum += matrix[i][j];
		}
		printf("\n");
	}
	printf("\nSum of all elements in matrix = %d",sum);
	getch();
}