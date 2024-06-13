package contacorrente;
public class ContaCorrente {
    // Atributos da conta corrente
    private final String nomeTitular;
    private double saldo;

    // Construtor da classe
    public ContaCorrente(String nomeTitular, double saldoInicial) {
        this.nomeTitular = nomeTitular;
        this.saldo = saldoInicial;
    }

    // Métodos para sacar e depositar
    public void sacar(double valor) {
        if (valor > 0 && valor <= saldo) {
            saldo -= valor;
            System.out.println("Saque realizado com sucesso. Saldo atual: " + saldo);
        } else {
            System.out.println("Saldo insuficiente para o saque.");
        }
    }

    public void depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
            System.out.println("Depósito realizado com sucesso. Saldo atual: " + saldo);
        } else {
            System.out.println("Valor inválido para depósito.");
        }
    }

    // Método para obter o saldo
    public double getSaldo() {
        return saldo;
    }
}