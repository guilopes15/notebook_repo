/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package a4ex10;

import java.util.Scanner;

/**
 *
 * @author guilherme
 */
public class A4ex10 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int vidas = 7;
        String p = args[0];
        String r = "";
        Scanner s = new Scanner(System.in);
        boolean gameOver;
        
        while (vidas>0){
            gameOver = true;
            for (int i = 0; i < p.length(); i++) {
                char x = p.charAt(i);
                if (r.matches(".*"+x+".*"))
                    System.out.print(x);
                else {
                    System.out.print("-");
                    gameOver = false;
                }
            }
            
            if (gameOver) {
                System.out.println("\nGanhou");
                break;
            }
            
            System.out.println(" Vidas"+vidas+", Digite uma letra: ");
            String l = s.next();
            if (!l.matches("[a-z]|[A-Z]"))
                continue;

            if (r.matches(".*"+l+".*")){
                System.out.println("Letra repetida");
                continue;
            }
            
            if (p.matches(".*"+l+".*")) {
            
                System.out.println("Acertou");
            
            } else {
                System.out.println("Errou");
                vidas--;
            
            }
        
            r += l;

        }
        
        System.out.println("Fim");
    }
    
}
