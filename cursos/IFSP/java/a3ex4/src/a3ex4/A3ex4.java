/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package a3ex4;
import javax.swing.JOptionPane;
/**
 *
 * @author guilherme
 */
public class A3ex4 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try {
            String valor = JOptionPane.showInputDialog("Digite a nota:");
            float nota = Float.parseFloat(valor);
            JOptionPane.showMessageDialog(null, "Nota digitada: " +nota);
            
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Houve um erro. Digite apenas numeros");
            // e.printStackTrace();
        }
    }
}
