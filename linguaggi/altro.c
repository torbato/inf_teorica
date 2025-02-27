#include <stdio.h>

/* int main() {
    int y;
    double x;

    x = 3.2;
    y = 5;

    printf("%g\n", x / 2);
    printf("quoziente: %d   resto: %d\n", y / 2, y % 2);

    x = y;
    printf("divisione reale: %g\n", x / 2);
} */

int main() {
    int a;
    int b;

    a = 2;
    b = 4;

    printf("a = %d\n", a);
    printf("b = %d\n", b);

    int c;

    c = a;
    a = b;
    b = c;

    printf("dopo l'inversione:\n");
    printf("a = %d\n", a);
    printf("b = %d\n", b);

    a = 2;

    printf("contenuto dell'indirizzo di a = %d\n", a);
    printf("etichetta dell'indirizzo di a = %u\n", &a);

    long d = (long) &a;

    printf("contenuto dell'indirizzo di d = %u\n", d);
    printf("etichetta dell'indirizzo di d = %u\n", &d);

    printf("cosa c'è all'indirizzo 264433548?: %u\n", (* (int *) d));


    // printf("%d\n", c);
}
