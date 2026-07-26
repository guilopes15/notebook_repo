/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package exercicio1aula4;

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 *
 * @author Guilherme Mendonça Lopes
 */
public class Exercicio1aula4 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        try {
            
            System.out.print("Digite o valor inicial: ");
            int valorInicial = s.nextInt();
            System.out.print("Digite o valor final: ");
            int valorFinal = s.nextInt();
            
            while (valorInicial <= valorFinal) {
            
                System.out.println(valorInicial++);   
            }
 
        }catch (InputMismatchException e){
            System.out.println("Digite apenas numeros inteiros!");

        }

   }
    
}
