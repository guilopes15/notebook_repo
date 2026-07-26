/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package a4ex9;

/**
 *
 * @author guilherme
 */
public class A4ex9 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // agrupadores 1 letra de a e z
        System.out.println("a".matches("[a-z]"));
        System.out.println("x".matches("[a-z]"));
        System.out.println("A".matches("[a-z]"));
        // 1 letra de a e Z, permitindo maiusculas
        System.out.println("a".matches("[a-z]|[A-Z]"));
        System.out.println("A".matches("[a-z]|[A-Z]"));
        System.out.println("x".matches("[a-z]|[A-Z]"));
        System.out.println("1".matches("[a-z]|[A-Z]"));
        // não pode começar com numero
        System.out.println("João".matches("[^0-9].*"));
        System.out.println("jp2018".matches("[^0-9]."));
        System.out.println("2018".matches("[^0-9]."));
        // não pode começar com letra
        System.out.println("2018".matches("[^a-z][A-Z].*"));
        System.out.println("2018jp".matches("[^a-z][A-Z].*"));
        System.out.println("jp2018".matches("[^a-z][^A-Z].*"));
        // validação de email
        System.out.println("jpescola@ifsp.edu.br".matches(".*@\\w{2,}[.]\\w{2,}.*"));
        System.out.println("jpescola@hmail.com".matches(".*@\\w{2,}[.]\\w{2,}.*"));
        System.out.println("jpescola@gmail".matches(".*@\\w{2,}[.]\\w{2,}.*"));
        System.out.println("jpescola@ifsp".matches(".*@\\w{2,}[.]\\w{2,}.*"));
    }
    
}
