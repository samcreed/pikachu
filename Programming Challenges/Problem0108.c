/*http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=44*/

int main()
{
    int N;
    scanf("%d", &N);

    int A[N][N];
    int S[N][N];
    int i, j;

    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    /*
    printf("You entered:\n\n");
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }
    */

    /* calculate sum of all rectangles */
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            if (i > 0 && j > 0) {
                /* general formula; add the two smaller rectangles and subtract the overlap */
                S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + A[i][j];
            } else if (i == 0 && j > 0) {
                /* single row/column vector sum */
                S[0][j] = S[0][j-1] + A[0][j];
            } else if (i > 0 && j == 0) {
                S[i][0] = S[i-1][0] + A[i][0];
            } else {
                S[0][0] = A[0][0];
            }
        }
    }

    /*
    printf("Sum table:\n\n");
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            printf("%d ", S[i][j]);
        }
        printf("\n");
    }
    */

    int i2, j2;
    int max = -999;
    int try;

    /* look at all possible differences */
    for (i2 = 0; i2 < N; i2++) {
        for (i = -1; i < i2; i++) {
            for (j2 = 0; j2 < N; j2++) {
                for (j = -1; j < j2; j++) {

                    if (i >= 0 && j >= 0) {
                        try = S[i2][j2] - S[i][j2] - S[i2][j] + S[i][j];
                    } else if (i == -1 && j >= 0) {
                        try = S[i2][j2] - S[i2][j];
                    } else if (i >= 0 && j == -1) {
                        try = S[i2][j2] - S[i][j2];
                    } else {
                        try = S[i2][j2];
                    }

                    max = (try > max) ? try : max;
                }
            }
        }
    }

    printf("%d", max);

    return 0;
}
