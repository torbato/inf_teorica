#include <stdlib.h>
#include <stdio.h>

struct stato
{
    char *nome;
};

struct citta
{
    char *nome;
    struct stato *stato;
};

int main()
{
    struct stato italia;
    struct citta roma;

    roma.nome = "Roma";
    roma.stato = &italia;

    italia.nome = "Italia";

    printf("%s\n", roma.stato->nome);

    return EXIT_SUCCESS;
}