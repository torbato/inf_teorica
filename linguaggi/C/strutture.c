#include <stdio.h>

struct persona
{
    char *nome;
    char *cognome;
    struct comune *residenza;
};

struct comune
{
    char *nome;
    char *codice;
    int abitanti;
};

int main()
{
    struct persona a;
    struct persona b;
    struct comune c;
    
    c.nome = "Roma";
    c.codice = "H501";
    c.abitanti = 44321435;

    a.nome = "Mario";
    a.cognome = "Rossi";
    a.residenza = &c;

    b.nome = "Luigi";
    b.cognome = "Bianchi";
    b.residenza = &c;

    printf("%d\n", (*a.residenza).abitanti);

}