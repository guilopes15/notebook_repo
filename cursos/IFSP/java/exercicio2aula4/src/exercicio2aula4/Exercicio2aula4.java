/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package exercicio2aula4;

import java.text.DecimalFormat;
import java.util.Scanner;

/**
 *
 * @author Guilherme Mendonça Lopes
 */
public class Exercicio2aula4 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        try {
            System.out.print("""
                         Digite uma operação(EX: soma, subtração, multiplicação, divisão, resto
                         da divisão, potência)""");
    
            String op = s.nextLine();
            op = op.toLowerCase().trim();
            System.out.print("Digite o primeiro valor:: ");
            double pValor = s.nextDouble();
            System.out.print("Digite o Segundo valor:: ");
            double sValor = s.nextDouble();
            double result = 0;
            switch (op) {

                case "soma": result= pValor + sValor; break;
                case "subtração": result=pValor - sValor; break;
                case "multiplição": result=pValor * sValor; break;
                case "divisão": result=pValor / sValor; break;
                case "resto da divisão": result=pValor % sValor; break;
                case "potência": result=Math.pow(pValor, sValor); break;

                default: break;
            }
       
            DecimalFormat df = new DecimalFormat("#.##");
            System.out.println(df.format(result));
            
        } catch (Exception e) {
            System.out.println("Erro! Verifique o Input e tente novamente");
        }
     
    }
    
}
