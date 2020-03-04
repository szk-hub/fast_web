package Fibonacci;

public class of {
    public static int of(int n){
        if(n==1||n==2){
            return 1;
        }
        return of(n-1)+of(n-2);
    }
    public static void main(String[] args){
        for(int i=1;i<=200;i++){
            System.out.println("Fibonacci.of("+i+") =="+of(i));
        }
    }
}
