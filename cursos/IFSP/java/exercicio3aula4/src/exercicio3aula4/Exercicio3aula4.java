/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package exercicio3aula4;

import java.util.Scanner;

/**
 *
 * @author Guilherme Mendonça Lopes
 */
public class Exercicio3aula4 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        System.out.print("Digite um texto: ");
        String texto = s.nextLine().toLowerCase();
        String novoTexto = "";
        
        for (char letra: texto.toCharArray()) {
            if (letra != 'a'){
                novoTexto += letra;
            }
        }
        
        System.out.println(novoTexto);
    }
    
}
