/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package a4ex5;

/**
 *
 * @author guilherme
 */
public class A4ex5 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        String frase = "Eu gosto de uva";
        
        System.out.println(frase.length());
        System.out.println(frase.charAt(3));
        System.out.println(frase.toUpperCase());
        System.out.println(frase.toLowerCase());
        System.out.println(frase.substring(3, 8)); // slice
        
        String novaFrase = " "+frase+" ";
        
        System.out.println(novaFrase);
        System.out.println(novaFrase.trim());
        System.out.println(frase.replace("uva", "manga"));
        System.out.println(frase.indexOf("m"));
                
        
    }
    
}
