import java.util.Scanner;

public class CalculadoraAceleracao {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Bem-vindo à Calculadora de Aceleração de Carro!");

        // Solicita ao usuário que defina a aceleração
        System.out.print("Digite a aceleração do carro (em metros por segundo ao quadrado): ");
        double aceleracao = scanner.nextDouble();

        // Solicita ao usuário que defina o tempo de aceleração
        System.out.print("Digite o tempo de aceleração (em segundos): ");
        double tempo = scanner.nextDouble();

        // Calcula a velocidade final usando a fórmula: v = u + at
        double velocidadeInicial = 0.0;  // Considerando que a velocidade inicial é zero
        double velocidadeFinal = velocidadeInicial + (aceleracao * tempo);

        // Exibe a velocidade final calculada
        System.out.println("A velocidade final do carro após " + tempo + " segundos de aceleração é: " + velocidadeFinal + " m/s");

        scanner.close();
    }
}
