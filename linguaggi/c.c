#include <stdio.h>

void altra() {
    printf("sono la funzione altra\n");}

void gigi(int a, int b) {
    printf("valori: %d %d\n", a, b);
}

int main() {
    int a, b;
    a = 9;
    printf("%d\n", a + 2);

    if (a > 0) {
        printf("positivo\n");
    }

    for (a = 0; a < 12; a += 2) {
        printf("%d ", a);
    }

    printf("\n");

    a = 1;
    b = 10;

    altra();

    gigi(a, b);
    gigi(b, a);
}
