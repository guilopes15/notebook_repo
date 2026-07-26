/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package a3ex6;
import javax.swing.JOptionPane;
/**
 *
 * @author guilherme
 */
public class A3ex6 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        String escolha = JOptionPane.showInputDialog("Digite V para verdadeiro e F para falso");
        if (escolha.equals("V") || escolha.equals("F")){
            JOptionPane.showMessageDialog(null, "Escolha: " +escolha);
        } else {
            JOptionPane.showMessageDialog(null, "Erro");
        }
    }
    
}
