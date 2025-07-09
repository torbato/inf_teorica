#include <stdio.h>

int main()
{
    printf("numeri con segno e senza segno\n");
    int x, y;
    x = 12;
    y = -12;
    printf("	due numeri, stampati con segno: %d %d\n", x, y);
    printf("	stessi, come fossero positivi:  %u %u\n", x, y);

    printf("\nrappresentazione binaria, con divisioni successive\n");
    unsigned z = 112, quoz, resto;
    quoz = z;
    while (quoz > 0)
    {
        printf("	%d %d %d\n", quoz, quoz / 2, quoz % 2);
        quoz = quoz / 2;
    }

    printf("\nrappresentazione binaria, con scorrimento e congiunzione\n");
    int i;
    printf("	");
    for (i = 31; i >= 0; i--)
        printf("%d", (z >> i) & 1);
    printf("\n");

    printf("\nnumeri frazionari, stampati in vari modi\n");
    double d;
    d = 1000;
    printf("	con %%d: %d\n", d);
    printf("	con %%d + cast: %d\n", (int)d);
    printf("	con %%e: %e\n", d);
    printf("	con %%g: %g\n", d);
}