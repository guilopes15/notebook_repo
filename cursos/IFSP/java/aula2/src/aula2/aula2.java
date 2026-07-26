/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula2;

// comentario

/* comentario
de varias
linhas
*/

public class aula2 {

    public static void main(String[] args) {
        System.out.print("primeiro argumento: " );
        System.out.print(args[0]);
        System.out.println("segundo argumento: " +args[1]);
        System.out.printf("segundo argumento: %s \n", args[1]);
        
        //
        
        char sexo = 'f'; // char ou String
        double nota = 5.5; // float ou double
        int alunos = 100, classes = 10; // int, short ou long
        boolean ativado = false;
    
        System.out.println("sexo: "+sexo);
        System.out.println("nota: "+nota);
        System.out.println("alunos: "+alunos);
        System.out.println("classes: "+classes+" situação? "+ativado);
        
        //
        
        final int IDADE = 10; // declaração de constante
        
        // incremento e decremento unitario
        int x = 5;
        x = ++x;
        x = x++;
        x = --x;
        x = x--;
        
        //
        
        int z = 10;
        int y = 3;
        System.out.println("x="+x);
        System.out.println("y="+y);
        System.out.println("-x"+(-x));
        System.out.println("x/y="+(x/y));
        System.out.println("Resto de x por y="+(x%y));
        System.out.println("Incremento de x="+(++x));
        
        // Conversão de tipos
        
        y = (float)x;
        y = Integer.parseInt(x);
        y =Float.parseFloat(x);
        y = Double.parseDouble(x);
        y = String.valueOf(x);
        y = ""+x;
        
        //
        
        int x = 10;
        double y = 3.5;
        char z = 'a';
        String v = "3.5";
        
        n = (int)y;
        System.out.println("n = "+n);
        n = Float.parseFloat(v);
        System.out.println("n = "+n);
        float a = (float)x;
        String idade = ""+x;
        System.out.println("Valor de a: "+a+", idade="+idade);
        
        
    }   
    
    
}
        
    
    
