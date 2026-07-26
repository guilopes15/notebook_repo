/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package a3ex3;

/**
 *
 * @author guilherme
 */
public class A3ex3 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try {
            float div = Integer.parseInt(args[0]) / Integer.parseInt(args[1]);
            System.out.println("resultado:" +div);
        } catch (ArrayIndexOutOfBoundsException e1){
            System.out.println("Passe 2 argumentos");
        }catch (ArithmeticException e2){
            System.out.println("Nao é possivel dividir por zero");
        } catch (Exception e3) {
            System.out.println("Houve um erro");
        }
        
        
        
    }
    
}
