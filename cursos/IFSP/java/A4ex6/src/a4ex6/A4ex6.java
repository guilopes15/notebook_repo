/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package a4ex6;

/**
 *
 * @author guilherme
 */
public class A4ex6 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Regex
        
        // Validação 1 char
        System.out.println("1".matches(".")); // true
        System.out.println("a".matches(".")); // true
        System.out.println("aa".matches(".")); //false
        // Validação 2 char
        System.out.println("ab".matches("..")); // true
        System.out.println("///".matches("..")); //false
        // 1 digito numerico
        System.out.println("1".matches("\\d.")); // true
        System.out.println("a1".matches("\\d.")); //false
        System.out.println("-9".matches("\\d")); //false
        // 2 digitos numericos
        System.out.println("10".matches("\\d\\d.")); // true
        System.out.println("100".matches("\\d\\d")); //false
        // 1 char e 1 gigito numerico
        System.out.println("a1".matches("\\w\\d")); // true
        System.out.println("aa1".matches("\\w\\d")); //false
        // 2 char e 1 digito numerico
        System.out.println("aa1".matches("\\w\\w\\d")); // true
        System.out.println("a11".matches("\\w\\w\\d")); // true
        System.out.println("111".matches("\\w\\w\\d")); // true
        System.out.println("11a".matches("\\w\\w\\d")); //false
        // 1 char especial
        System.out.println("@".matches("\\W")); // true
        System.out.println(".".matches("\\W")); // true
        System.out.println("/".matches("\\W")); // true
        System.out.println("%/".matches("\\W")); //false
        // espaço em branco
        System.out.println(" ".matches("\\s")); // true
        System.out.println("  ".matches("\\s")); //false
        
    }
    
}
