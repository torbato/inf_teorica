class Persona {
    String nome;
    int nascita;
}

class Classe {
    public static void main(String args[]) {
        Persona a;
        a = new Persona();

        a.nome = "Mario";
        a.nascita = 1993;

        System.out.println(a.nome + " " + a.nascita);
    }
}