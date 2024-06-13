package data;

import java.util.Calendar;

public class Data{
    public static void main(String[] args) {
        Calendar calendario = Calendar.getInstance();

        int dia = calendario.get(Calendar.DAY_OF_MONTH);
        int mes = calendario.get(Calendar.MONTH) + 1; // Adicione 1, pois o mês começa em 0 (janeiro).
        int ano = calendario.get(Calendar.YEAR);

        System.out.println("Data atual: " + dia + "/" + mes + "/" + ano);
    }
}
