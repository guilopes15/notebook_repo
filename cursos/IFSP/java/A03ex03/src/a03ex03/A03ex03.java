/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package a03ex03;

import javax.swing.JOptionPane;

/**
 *
 * @author guilherme
 */
public class A03ex03 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        String largura = JOptionPane.showInputDialog(null, "Digite a altura", "Guilherme", JOptionPane.QUESTION_MESSAGE);
        String altura = JOptionPane.showInputDialog("Digite a largura");
        float area = Float.parseFloat(largura) * Float.parseFloat(altura);
        float tijolos = area * 20;
        String status = "";
        
        if (area < 3){
            status = "baixa";
        } else if (area > 3.5){
            status = "alta";       
        }else {
           status = "media";
        }
           
        JOptionPane.showMessageDialog(
                null, 
                "Tijolos necessarios: " +tijolos+ "\nA parede é considerada " +status, 
                "Guilherme", 
                JOptionPane.INFORMATION_MESSAGE
        );
    
    }
    
}
