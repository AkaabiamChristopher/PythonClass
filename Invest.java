import java.util.Scanner;

public class Interest{
public static void main(String[] args) {
  Scanner input = new Scanner(System.in);


     System.out.print("Enter invest amount: ");
     double investmentAmount = input.nextDouble();

      System.out.print("Enter the annual interest rate: ");
      double annualInterestrate = input.nextDouble(); 

       System.out.print("Enter the number of yesrs : ");
      double numberOfyears = input.nextDouble(); 



      double result = annualAmountt * annualinterstRate /12;
      System.out.printf("the interest is %.2f", result);




      }

 }