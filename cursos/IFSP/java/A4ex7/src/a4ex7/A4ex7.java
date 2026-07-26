/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package a4ex7;

/**
 *
 * @author guilherme
 */
public class A4ex7 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // 2 digitos numericos
        System.out.println("12".matches("\\d{2}"));
        System.out.println("12".matches("\\d{3}"));
        // 2 digitos ou mais
        System.out.println("12".matches("\\d{2,}"));
        System.out.println("123".matches("\\d{2,}"));
        System.out.println("1".matches("\\d{2,}"));
        // limitando de 2 a 3 digitos
        System.out.println("12".matches("\\d{2,3}"));
        System.out.println("123".matches("\\d{2,3}"));
        System.out.println("1".matches("\\d{2,3}"));
        System.out.println("1234".matches("\\d{2,3}"));
        // validação de cep
        System.out.println("14781-000".matches("\\d{5}-\\d{3}"));
        System.out.println("14781000".matches("\\d{5}-\\d{3}"));
        System.out.println("14781000".matches("\\d{5}-\\d{3}"));
        System.out.println("14.781-000".matches("\\d{5}-\\d{3}"));
        // validação de data
        System.out.println("1/2/2000".matches("\\d{1,}/\\d{1,}/\\d{4}"));
        System.out.println("01/01/2000".matches("\\d{1,}/\\d{1,}/\\d{4}"));
        System.out.println("27/02/1889".matches("\\d{1,}/\\d{1,}/\\d{4}"));
        System.out.println("27/02/89".matches("\\d{1,}/\\d{1,}/\\d{4}"));
        
    }
    
}
