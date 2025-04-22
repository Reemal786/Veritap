// can ready pyhton script using scanner
import java.util.Scanner;

public class RFIDReader { //method for running python script and getting UID from card
    public static String readUID() {
        String UID = null; //variable for holding UID number

        try { //running the python script
            ProcessBuilder builder = new ProcessBuilder("python3", "/home/hoorr/read_rfid.py"); 
            //running Python and telling where to find the python script that cans RFID
            Process process_rfid = builder.start(); //starts the python script and allows access to it

            // Read the result (the UID) from the script output by using scanner
            Scanner scanner_output = new Scanner(process_rfid.getInputStream());

            while(scanner_output.hasNextLine()) { //checks sif script printed anything
                String UID_number = scanner_output.nextLine().trim(); //if so,gets rid of any extra spaces
                //and saves it to variable UID variable
                if (UID_number.matches("\\d+")){//check if the line contains only digits
                    UID = UID_number;//if so, assign UID number to UID variable
                    break;//once UID number is found, stop the loop
                }
            }

            scanner_output.close(); //closing scanner
            process_rfid.waitFor(); // waits for script to finish running
        } 
        catch (Exception error_rfid) {//if anything goes wrong, store the error in the wrror variable 
            //and print the error below
            System.out.println("Error reading UID: " + error_rfid.getMessage());
        }

        return UID;//return but dont print the value of the UID
    }
}
