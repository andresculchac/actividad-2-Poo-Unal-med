package org.example;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        double obtenerArea, obtenerPerimetro, valorAltura2;
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese el lado del triangulo");
        int lado = entrada.nextInt();

        obtenerArea = Triangulo.area(lado);
        obtenerPerimetro = Triangulo.perimetro(lado);
        valorAltura2 = Triangulo.valorAltura(lado);

        System.out.println("El area del triangulo es " + obtenerArea + "cm");
        System.out.println("El perimetro del triangulo es " + obtenerPerimetro+ "cm");
        System.out.println("la altura del triangulo es " + valorAltura2+ "cm");
    }
}