package calculandoareadotriangulo;
import java.util.Scanner;

public class CalculandoAreaTriangulo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Informe a base do triângulo: ");
        float base = (float) sc.nextFloat();
        System.out.print("Informe a altura do triângulo: ");
        float altura = (float) sc.nextFloat();

        float area = (float) (0.5 * base * altura);
        System.out.println("A área do triângulo é: " + area);

        sc.close();
    }
}
