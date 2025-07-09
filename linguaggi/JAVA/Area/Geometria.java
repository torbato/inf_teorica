class Rettangolo {
    int base;
    int altezza;
}

class Quadrato extends Rettangolo {
    // base = altezza;
}

class Geometria {
    static int area(Rettangolo r) {
        return r.base * r.altezza;
    }

    public static void main(String args[]) {
        Quadrato q = new Quadrato();
        q.base = 2;
        q.altezza = 2;
        System.out.println("area del quadrato: " + area(q));

        Rettangolo r = new Rettangolo();
        r.base = 3;
        r.altezza = 100;
        System.out.println("area del rettangolo: " + area(r));
    }
}

