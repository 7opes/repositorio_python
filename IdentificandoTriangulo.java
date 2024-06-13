package identificandotriangulo;
import java.util.Scanner;

public class IdentificandoTriangulo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Informe a primeira medida: ");
        int a = sc.nextInt();
        System.out.print("Informe a segunda medida: ");
        int b = sc.nextInt();
        System.out.print("Informe a terceira medida: ");
        int c = sc.nextInt();

        if ((a + b > c) && (a + c > b) && (b + c > a)) {
            if (a == b && a == c) {
                System.out.println("Triângulo equilátero.");
            } else if (a == b || a == c || b == c) {
                System.out.println("Triângulo isósceles.");
            } else {
                System.out.println("Triângulo escaleno.");
            }
        } else {
            System.out.println("Não forma um triângulo.");
        }

        sc.close();
    }
}

