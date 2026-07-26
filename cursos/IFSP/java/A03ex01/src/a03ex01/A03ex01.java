/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package a03ex01;

import java.util.Scanner;

/**
 *
 * @author guilherme
 */
public class A03ex01 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Digite a largura:");
        float largura = s.nextFloat();
        System.out.println("Digite a altura");
        float altura = s.nextFloat();  
        float area = largura * altura;
        float tijolos = area * 20;
        System.out.println("Tijolos necessarios:" +tijolos);
    }
    
}
