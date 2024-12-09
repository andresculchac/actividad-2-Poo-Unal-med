package org.example;

public class Triangulo {
    public static double obtener_perimetro(double la, double lb, double lc){
        return  la + lb + lc;
    }
    public static double obtener_semiperimetro(double p){
        return p/2;
    }
    public static double obtener_area(double s, double la, double lb, double lc){
        return Math.sqrt(s*(s-la) * (s-lb) * (s-lc));
    }
}
