class Primo {
    int x;
}

class Secondo {
    int x;
}

class Main {
    static void esempio(Primo p) {
        System.out.println(p.x);
    }

    public static int main(String[] args) {
        prima = new Primo();
        seconda = new Secondo();
        prima.x = 12;
        seconda.x = 3;
        
        esempio(seconda);
    }
}