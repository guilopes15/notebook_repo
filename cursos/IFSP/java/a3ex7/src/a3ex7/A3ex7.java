/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package a3ex7;

/**
 *
 * @author guilherme
 */
public class A3ex7 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        if (args.length > 0){
            String info="";
            switch (args[0]){
                case "1": info="Domingo"; break;
                case "2": info="Segunda"; break;
                case "3": info="Terça"; break;
                case "4": info="Quarta"; break;
                case "5": info="Quinta"; break;
                case "6": info="Sexta"; break;
                case "7": info="Sabado"; break;
                default: info="Argumento invalido";
                
            }
            System.out.println(info);
        }
        else{
            System.out.println("Argumneto numerico obrigatorio");
            
            
        }
    }
    
}
