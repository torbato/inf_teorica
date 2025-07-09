// CICLI

// #include <stdio.h>

// int main() {
//     int i;

//     for (i = 0; i < 10; i++)
//             printf("%d\n", i);
// }

// FUNZIONI

// #include <stdio.h>

// int subtract(int a, int b) {
//     return a - b;
// };

// int main() {
//     int a = 12;
//     int b = 3;

//     printf("%d\n", subtract(b, a));
// }

// VARIABILI REALI

// #include <stdio.h>

// int main() {
//     int a;
//     double b;
//     double *c;

//     a = 12;
//     b = 12.2;

//     printf("a: %d\n", a);
//     printf("b: %g\n", b);

//     printf("indirizzo e grandezza di a: %u %lu\n", &a, sizeof(a));
//     printf("indirizzo e grandezza di b: %u %lu\n", &b, sizeof(b));

//     c = &b;
//     printf("valore di *c: %g\n", *c);
// }

// CARATTERI

// #include <stdio.h>

// int main() {
//     int a;
//     char b;
//     char *c;

//     a = 12;
//     b = 'x';

//     printf("a: %d\n", a);
//     printf("b: %c\n", b);

//     printf("indirizzo e grandezza di a: %u %u\n", &a, sizeof(a));
//     printf("indirizzo e grandezza di b: %u %u\n", &b, sizeof(b));

//     c = &b;
//     printf("valore di *c: %c\n", *c);
// }

// VETTORI

// #include <stdio.h>

// int main() {
//     int a[4];
//     int i;

//     a[0] = 31;
//     a[1] = 1;
//     a[2] = 7;
//     a[3] = 4;

//     printf("secondo elemento del vettore: %d\n", a[1]);

//     for (i = 0; i < 4; i++)
//         printf("indice %d, valore %d\n", i, a[i]);
// }

// STRINGHE

// #include <stdio.h>

// int main() {
//     char *s;

//     s = "hello";

//     printf("stringa: %s\n", s);
//     printf("secondo carattere: %c\n", s[1]);
// }

// VETTORI DI STRINGHE

#include <stdio.h>

int main() {
    char *a[3];
    int i;

    a[0] = "un";
    a[1] = "esempio";
    a[2] = "qui";

    printf("secondo carattere del secondo elemento: %c\n", a[1][1]);

    for (i = 0; i < 3; i++)
        printf("%s\n", a[i]);
}