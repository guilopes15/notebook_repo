/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package exercicio4aula4;

import java.util.Scanner;

/**
 *
 * @author Guilherme Mendonça Lopes
 */
public class Exercicio4aula4 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        String[] pLista = {"pizza", "lasanha", "churrasco"};
        System.out.println("Qual seu prato preferido?");
        String input = s.nextLine().toLowerCase();
        String negativa = "Disso eu não gosto muito!";
        
        boolean encontrado = false;
        
        
        for (String item: pLista) {
            if (input.matches(".*\\b"+item+"\\b.*")){
                System.out.println("Eu adoro "+input);
                encontrado = true;
                break;
            } 
        }   
        if (!encontrado) {
            System.out.println(negativa);
            
        }
        
        encontrado = false;
        String[] sLista = {"futebol", "basquete", "tenis"};
        System.out.println("Qual seu esporte favorito?");
        input = s.nextLine().toLowerCase();
        
     
        for (String item: sLista) {
            if (input.matches(".*\\b"+item+"\\b.*")){
                System.out.println("Eu adoro "+input);
                encontrado = true;
                break;
            } 
        }   
        if (!encontrado) {
            System.out.println(negativa);
            
        }
        
        encontrado = false;
        String[] tLista = {"java", "python", "javascript"};
        System.out.println("Qual sua linguagem de programação favorita?");
        input = s.nextLine().toLowerCase();
         
        for (String item: tLista) {
            if (input.matches(".*\\b"+item+"\\b.*")){
                System.out.println("Eu adoro "+input);
                encontrado = true;
                break;
            } 
        }   
        if (!encontrado) {
            System.out.println(negativa);
            
        }
    
    }
    
}
