package org.example;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {



        int retencion_fuente;
        String nombre, apellido, nombre_empleado;

        double salario_bruto;
        double salario_neto;
        double valor_hora_trabajada_mes;

        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrese el codigo del empleado");
        int codigo_empleado = entrada.nextInt();

        System.out.println("Ingrese el nombre del empleado");
        nombre = entrada.next();

        System.out.println("Ingrese el apellido del empleado");
        apellido = entrada.next();
        nombre_empleado = nombre+ " " + apellido;

        System.out.println("Ingrese el numero de las horas trabajadas al mes");
        double numero_horas_trabajadas_mes = entrada.nextDouble();

        System.out.println("Ingrese el valor de la hora trabajada");
        valor_hora_trabajada_mes = entrada.nextDouble();

        System.out.println("Ingrese el valor de la retencion");
        double porcentaje_retencion = entrada.nextDouble();



        porcentaje_retencion = Empleado.calcular_porcentaje_retencion(porcentaje_retencion);
        salario_bruto= Empleado.calcular_salario_bruto(40,90000);
        salario_neto= Empleado.salario_neto(salario_bruto,porcentaje_retencion);

        System.out.println("Codigo: " + codigo_empleado);
        System.out.println("Nombre: " + nombre_empleado);
        System.out.println("Salario Bruto: " + salario_bruto);
        System.out.println("Salario neto: " + salario_neto);


    }
}