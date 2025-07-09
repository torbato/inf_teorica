class Persona {
    String nome;
    int anno;
}

class Monumento {
    String nome;
    int anno;
}

class Sovraccarico {
    static void stampa(Persona p) {
        System.out.println(p.nome + " " + p.anno);
    };

    static void stampa(Monumento m) {
        System.out.println(m.nome + " " + m.anno);
    };

    public static void main(String args[]) {

        Persona a = new Persona();
        Persona b = new Persona();
        Monumento c = new Monumento();

        a.nome = "Mario";
        a.anno = 1993;
        stampa(a);

        b.nome = "Luigi";
        b.anno = 2001;
        stampa(b);

        c.nome = "Mausoleo di Augusto";
        c.anno = 2017;
        stampa(c);
    }
}
