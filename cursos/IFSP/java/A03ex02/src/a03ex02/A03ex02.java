/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package a03ex02;

import javax.swing.JOptionPane;

/**
 *
 * @author guilherme
 */
public class A03ex02 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        String largura = JOptionPane.showInputDialog(null, "Digite a altura", "Guilherme", JOptionPane.QUESTION_MESSAGE);
        String altura = JOptionPane.showInputDialog("Digite a largura");
        float area = Float.parseFloat(largura) * Float.parseFloat(altura);
        float tijolos = area * 20;
        JOptionPane.showMessageDialog(null, "Tijolos necessarios: " +tijolos, "Guilherme", JOptionPane.INFORMATION_MESSAGE);
    }
    
}
