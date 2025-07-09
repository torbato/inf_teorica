class Persona {
    String nome;
    int anno;

    void stampa() {
        System.out.println("nome: " + nome);
        System.out.println("anno di nascita: " + anno);
    }
}

class Operaio extends Persona {
    String qualifica;

    @Override
    void stampa() {
        //super.stampa();
        System.out.println("qualifica: " + qualifica);
    }
}

class Archeologo extends Persona {
    int laurea;
}

class Monumento {
    String nome;
    int anno;

    void stampa() {
        System.out.println("nome: " + nome);
        System.out.println("anno di ultimo intervento: " + anno);
    }
}

class Sottoclasse {
    public static void main(String args[]) {
        Persona a = new Persona();
        Persona b = new Persona();
        Monumento c = new Monumento();
        Operaio d = new Operaio();

        a.nome = "Mario";
        a.anno = 1928;
        a.stampa();

        b.nome = "Luca";
        b.anno = 2014;
        b.stampa();

        c.nome = "Mausoleo di Augusto";
        c.anno = 2017;
        c.stampa();
        
        d.nome = "Luca";
        d.anno = 2003;
        d.qualifica = "scavi";
        d.stampa();
        
    }
}