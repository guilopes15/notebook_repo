/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package a4ex8;

/**
 *
 * @author guilherme
 */
public class A4ex8 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // prontuario começa com 18
        System.out.println("185566".matches("^18."));
        System.out.println("18".matches("^18."));
        System.out.println("181".matches("^18."));
        System.out.println("155566".matches("^18."));
        // termina com 2018
        System.out.println("01/01/2018".matches(".*2018$"));
        System.out.println("2018".matches(".*2018$"));
        System.out.println("aaaa2018".matches(".*2018$"));
        System.out.println("aaaa2018".matches(".*2018$"));
        // procura 2018 no texto
        System.out.println("aaaa2018a".matches(".*2018.*"));
        System.out.println("Eu nasci em 2018".matches(".*2018.*"));
        System.out.println("Em 2018 farei 10 anos".matches(".*2018.*"));
        System.out.println("Em 20 18 farei 10 anos".matches(".*2018.*"));
        // pesquisa uma lista de palavras
        System.out.println("sim".matches("sim|não"));
        System.out.println("não".matches("sim|não"));
        System.out.println("não".matches("sim|não"));
        System.out.println("talzez".matches("sim|não"));
        
        
    }
    
}
