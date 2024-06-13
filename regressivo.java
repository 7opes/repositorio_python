public class regressivo{
    public static void main(String[] args) {
        Contador c1 = new Contador();
        do{
        c1.decrementar();
        System.out.println(c1.valor);
        } while (c1.valor>0);
    }
}