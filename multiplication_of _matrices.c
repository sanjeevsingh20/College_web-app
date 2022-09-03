// to multiply two matrix

#include <stdio.h>

int main()
{
    int matrix1[100][100], matrix2[100][100], multiplicaton[100][100];
    int rows1, column1, rows2, column2;
    printf("Enter the number of rows of matrix 1: ");
    scanf("%d", &rows1);
    printf("Enter the number of columns of matrix 1: ");
    scanf("%d", &column1);
    printf("Enter the number of rows of matrix 1: ");
    scanf("%d", &rows2);
    printf("Enter the number of columns of matrix 1: ");
    scanf("%d", &column2);
    if (column1 == rows2)
    {
        printf("Enter the values of matrix 1:\n\n");
        for (int i = 0; i < rows1; i++)
        {
            for (int j = 0; j < column1; j++)
            {
                printf("Enter the value of a%d%d: ", i + 1, j + 1);
                scanf("%d", &matrix1[i][j]);
            }
        }
        printf("Enter the values of matrix 2:\n\n");
        for (int i = 0; i < rows2; i++)
        {
            for (int j = 0; j < column2; j++)
            {
                printf("Enter the value of a%d%d: ", i + 1, j + 1);
                scanf("%d", &matrix2[i][j]);
            }
        }
    }
    printf("\n\n");

    // multiplication of two matrices
    for (int i = 0; i < rows1; i++)
    {
        for (int k = 0; k < column2; k++)
        {
            for (int j = 0; j < column1; j++)
            {
                multiplicaton[i][k] += matrix1[i][j] * matrix2[j][k];
            }
        }
    }

    // printing the multiplication
    printf("The multiplication of matrix1 and matrix2 is \n\n");
    for (int k = 0; k < rows1; k++)
    {
        for (int l = 0; l < column2; l++)
        {
            printf("%d  ", multiplicaton[k][l]);
            if (l == column2 - 1)
            {
                printf("\n\n");
            }
        }
    }

    return 0;
}