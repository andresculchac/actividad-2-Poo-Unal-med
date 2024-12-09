package org.example;

public class Triangulo {
    public static int  perimetro(int lado){
        return lado*3;
    }
    public static double valorAltura (double lado){
        return Math.sqrt(Math.pow(lado,2)-(Math.pow(lado/2,2)));
    }
    public static double area(double lado){
        double altura = valorAltura(lado);
        return (altura*lado)/2;
    }
}
