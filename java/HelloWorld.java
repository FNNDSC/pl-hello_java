
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class HelloWorld {

    public static void main(String[] args) 
         throws IOException {
    
        // Prints "Hello, Name" to the terminal window.
        
        System.out.println("A simple java program to greet a user\n");
        if(args.length>1 ){
            int n = Integer.parseInt(args[1]);
            for(int i=0; i<n; i++)
                System.out.println("Hello "+ args[0]);
        }
        else
            System.out.println("Hello "+ args[0]);
    }

}



  

