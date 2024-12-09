package org.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        double la, lb, lc; //lado a, lado b y lado c del triangulo
        double p, s;
        double a; // area del triangulo

        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrese el valor del lado a");
        la = entrada.nextDouble();

        System.out.println("Ingrese el valor del lado b");
        lb = entrada.nextDouble();

        System.out.println("Ingrese el valor del lado c");
        lc = entrada.nextDouble();

        p = Triangulo.obtener_perimetro(la, lb, lc);
        s = Triangulo.obtener_semiperimetro(p);
        a = Triangulo.obtener_area(s, la, lb, lc);


        System.out.println("perimetro "+p);
        System.out.println("semiperimetro "+s);
        System.out.println("area "+a);
    }
}