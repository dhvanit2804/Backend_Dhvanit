#include<stdio.h>
#include<conio.h>

void main()
{
	int rno, s1, s2, s3, total;
	clrscr();
	double per;
	char sname[50];
	printf("\nEnter Student Name : ");
	gets(sname);
	printf("\nEnter Roll No : ");
	scanf("%d",&rno);
	printf("\nEnter Marks Of Subject 1 : ");
	scanf("%d",&s1);
	printf("\nEnter Marks Of Subject 2 : ");
	scanf("%d",&s2);
	printf("\nEnter Marks Of Subject 3 : ");
	scanf("%d",&s3);
	total = s1+s2+s3;
	per = total/3;
	printf("\nStudent Name : %s",sname);
	printf("\nRoll No : %d",rno);
	printf("\nTotal : %d",total);
	printf("\nPercentage : %lf",per);

	if(per>=70)
	{
		printf("\nDistinaction");
	}
	else if(per>=60)
	{
		printf("\nFirst Class");
	}
	else if(per>=50)
	{
		printf("\nSecond Class");
	}
	else if(per>=40)
	{
		printf("\nThird Class");
	}
	else
	{
		printf("\Fail");
	}
	getch();
}