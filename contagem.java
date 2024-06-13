public class contagem{
    public static void main(String[] args) {
        Contador c1 = new Contador();
        do{
        c1.incrementar ();
        System.out.println(c1.valor);
        } while (c1.valor<100);
    }
}