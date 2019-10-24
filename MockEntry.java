package mock;

import java.util.Scanner;
import mock.RSA;

public class MockEntry {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int p = 0;
		int q = 0;
		
		Double pt = new Double(0);
		Double ct = new Double(0);
		
		Scanner input = new Scanner(System.in);
		RSA rsa = new RSA();
		
		System.out.println("Enter prime values for P and Q\n");
		
		System.out.println("Value of P: \n");
		p = input.nextInt();
		
		System.out.println("Value of Q: \n");
		q = input.nextInt();
		
		int [] keys;
		keys = rsa.genRSAKeys(p, q);
		
		if(keys != null) {
			System.out.println("Public Key is: (" + keys[0] + ", " + keys[1] + ")");
		
			System.out.println("Private Key is: (" + keys[0] + ", " + keys[2] + ")");
			
			System.out.println("Enter plaintext: ");
			pt = input.nextDouble();
			
			ct = rsa.encryptRSA(pt, keys, p, q);
			System.out.println("Ciphertext is: " + ct.intValue());
			//Integer.parseInt(Double.toString(ct)));
			
			pt = rsa.decryptRSA(ct, keys, p, q);
			System.out.println("Decrypted Plaintext is: " + pt.intValue());
			//Integer.parseInt(Double.toString(pt)));
		}
		input.close();
	}

}
