class Persona {
    String nome; // nome della persona
    int anno; // anno di nascita
}

class Monumento {
    String nome; // nome del monumento
    int anno; // anno dell'ultimo restauro
}

class Due {
    static void stampa(Persona p) {
        System.out.println(p.nome + " " + p.anno);
    }

    public static void main(String args[]) {
        Persona a = new Persona();
        Persona b = new Persona();
        Monumento c = new Monumento();

        a.nome = "Mario";
        a.anno = 1993;
        stampa(a);

        b.nome = "Luca";
        b.anno = 2001;
        stampa(b);

        c.nome = "Mausoleo di Augusto";
        c.anno = 2017;
        System.out.println(c.nome + " " + c.anno);
    }
}