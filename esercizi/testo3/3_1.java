class Primo {
    int x;
}

class Secondo {
    int x;
}

class Main {
    static void azzera(Primo a) {
        a.x = 0;
    }

    public static void main(String[] args) {
        Primo a = new Primo();
        Secondo b = new Secondo();

        a.x = 12;
        azzera(a);

        b.x = 5;
        azzera(b);
    }
}