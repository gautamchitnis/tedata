package mock;

import java.util.Scanner;

public class RSA {

	public static int[] genRSAKeys(int p, int q) {
		int n = 0;
		int e = 0;
		int [] keys = new int[3];
		int phiN = 0;
		
		n = p*q;
		
		keys[0] = n;
		
		phiN = (p-1)*(q-1);
		
		for(int i=2;i<=phiN;i++) {
			if(i%phiN != 0) {
				System.out.println("\nPossible value for public key: "+i);
			}
		}
		
		System.out.println("Enter one value from possible public key values above: ");
		
		Scanner input1 = new Scanner(System.in);
		
		e = input1.nextInt();
		
		if(e == 0){
			System.out.println("Error in calculating public key");
			return null;
		} 
		
		keys[1] = e;
		
		int j;
		for(j=0;j<phiN;j++) {
			int tempVal = (e * j) % phiN;
			if(tempVal==1) {
				break;
			}
		}
		
		keys[2] = j;
		
		return keys;
	}
	
	public static double encryptRSA(double pt, int keys[], int p, int q) {
		Double dpte = Math.pow(pt, Double.valueOf(keys[1]));
		double ct = dpte%Double.valueOf(keys[0]);
		return ct;
	}
	
	public static double decryptRSA(double ct, int keys[], int p, int q) {
		Double dcte = Math.pow(ct, Double.valueOf(keys[2]));
		int n = p*q;
		double pt = dcte%Double.valueOf(keys[0]);
		return pt;
	}
}