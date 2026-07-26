/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package a3ex1;

import java.util.Scanner;

/**
 *
 * @author guilherme
 */
public class A3ex1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try {
        
            System.out.println("Digite a nota:");
            Scanner s = new Scanner(System.in);
            float nota = s.nextFloat();
            System.out.println("nota digitada: "+nota);
    
        }
        catch (Exception e) {
            System.out.println("Houve um erro. Difite apenas numeros!");
            // e.printStackTrace();
        }
    
    }
}