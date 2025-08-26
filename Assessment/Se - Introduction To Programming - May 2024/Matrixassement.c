#include <stdio.h>

void inputMatrix(int mat[10][10], int row, int col) {
    int i, j;
    printf("\nEnter elements of matrix (%d x %d):\n", row, col);
    for(i = 0; i < row; i++) {
        for(j = 0; j < col; j++) {
            printf("Enter element [%d][%d]: ", i+1, j+1);
            scanf("%d", &mat[i][j]);
        }
    }
}

void displayMatrix(int mat[10][10], int row, int col) {
    int i, j;
    printf("\nMatrix (%d x %d):\n", row, col);
    for(i = 0; i < row; i++) {
        for(j = 0; j < col; j++) {
            printf("%5d", mat[i][j]);
        }
        printf("\n");
    }
}

void multiplyMatrix(int a[10][10], int b[10][10], int result[10][10], int r1, int c1, int c2) {
    int i, j, k;

    for(i = 0; i < r1; i++) {
        for(j = 0; j < c2; j++) {
            result[i][j] = 0;
        }
    }

    for(i = 0; i < r1; i++) {
        for(j = 0; j < c2; j++) {
            for(k = 0; k < c1; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}

int main() {
    int a[10][10], b[10][10], result[10][10];
    int r1, c1, r2, c2;

    printf("----- Matrix Multiplication Program -----\n");

    // Input rows and columns for first matrix
    printf("\nEnter rows and columns for first matrix: ");
    scanf("%d%d", &r1, &c1);

    // Input rows and columns for second matrix
    printf("Enter rows and columns for second matrix: ");
    scanf("%d%d", &r2, &c2);

    // Check multiplication condition
    if(c1 != r2) {
        printf("\nMatrix multiplication is not possible!");
        printf("\n(Number of columns of first matrix must equal rows of second matrix)\n");
        return 0;
    }

    inputMatrix(a, r1, c1);
    inputMatrix(b, r2, c2);

    displayMatrix(a, r1, c1);
    displayMatrix(b, r2, c2);

    multiplyMatrix(a, b, result, r1, c1, c2);

    printf("\nResultant Matrix after multiplication:\n");
    displayMatrix(result, r1, c2);

    return 0;
}

