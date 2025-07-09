import java.util.LinkedList;

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
        // super.stampa();
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

class Lista {
    public static void main(String args[]) {
        Persona a = new Persona();
        Persona b = new Persona();
        Monumento c = new Monumento();
        Operaio d = new Operaio();

        LinkedList l = new LinkedList();
        l.add(a);
        l.add(b);
        l.add(d);
    
        for (Persona p : l)
			p.stampa();
    
    }
}