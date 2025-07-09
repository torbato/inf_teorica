#include <stdio.h>
#include <stdlib.h>

int main() {
    int *c;
    c = malloc(4);
    *c = 9;
    printf("%d\n", *c);
    free(c);
}