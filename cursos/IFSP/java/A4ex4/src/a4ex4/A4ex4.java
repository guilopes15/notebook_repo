/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package a4ex4;

import java.text.DecimalFormat;

/**
 *
 * @author guilherme
 */
public class A4ex4 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        DecimalFormat df = new DecimalFormat("#.###");
        
        // DecimalFormat df = (DecimalFormat).NumberFormat.getNumberInstance(Locale.getDefault());
        
        double n = (double)1/6;
        
        System.out.println(n);
        
        System.out.println(df.format(n));
        
    }
    
}
