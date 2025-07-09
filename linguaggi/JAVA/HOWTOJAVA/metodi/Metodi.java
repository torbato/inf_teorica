class Persona {
    String nome;
    int anno;

    void stampa() {
        System.out.println(nome + " " + anno);
    }

    @Override
    public String toString() {
        return(nome + " " + anno);
    }
}

class Metodi {
    public static void main(String args[]) {
        Persona a = new Persona();

        a.nome = "Mario";
        a.anno = 1999;

        // a.stampa();
        System.out.println(a);
    }
}