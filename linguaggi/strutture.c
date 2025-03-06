#include <stdio.h>

struct persona {
    char *nome;
    char *cognome;
    struct citta *residenza;
};

struct citta {
    char *nome;
    char *codice;
    int abitanti;
};

void stampapersona(struct persona p) {
    printf("si chiama %s %s e risiede a %s\n",
        p.nome, p.cognome, (*p.residenza).nome);
}

void stampacitta(struct citta c) {
    printf("città: %s, codice: %s, abitanti: %d\n", c.nome, c.codice, c.abitanti);
};

int main() {
    struct persona p1;
    struct persona p2;
    struct citta c1;

    c1.nome = "Roma";
    c1.codice = "H501";
    c1.abitanti = 2748165;
    stampacitta(c1);

    p1.nome = "Luca";
    p1.cognome = "Bianchi";
    p1.residenza = &c1;
    stampapersona(p1);

    p2.nome = "Mario";
    p2.cognome = "Rossi";
    p2.residenza = &c1;
    stampapersona(p2);

    // stampare il numero di abitanti della città di Luca
    // Luca vive in una grande città? più di 500000 abitanti?
    printf("Abitanti della città di Luca: %d\n", (*p1.residenza).abitanti);
}
