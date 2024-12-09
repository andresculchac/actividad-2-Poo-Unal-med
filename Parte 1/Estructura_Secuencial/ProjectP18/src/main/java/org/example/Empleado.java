package org.example;

public class Empleado {
    public static double calcular_porcentaje_retencion(double retencion){
        return retencion/100;
    }
    public static double calcular_salario_bruto(double numero_horas_trabajadas_mes, double valor_hora_trabajada) {
        return valor_hora_trabajada * numero_horas_trabajadas_mes;
    }
    public static double salario_neto(double salario_bruto, double porcentaje_retencion){
        return salario_bruto-(salario_bruto*porcentaje_retencion);
    }
}
