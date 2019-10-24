//============================================================================
// Name        : CRT_1.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include<iostream>
using namespace std;

int calc_inv(int a, int b)
{
	int x, y; 
        int b0 = b, t, q;
	int x0 = 0, x1 = 1;
	if (b == 1) 
		return 1;
	while (a > 1) 
	{
	    q = a / b;
	    t = b, 
	    b = a % b, 
	    a = t;
	    t = x0, 
	    x0 = x1 - q * x0, 
	    x1 = t;
	}
	if (x1 < 0) x1 += b0;
	return x1; 	
}

int main()
{	
	int i,n, a[10], b[10], m[10], m_inv[10], prod = 1, sum = 0;
	cout<< "\n Enter the numer of equations";
	cin >>n;
	for(i=0;i<n;i++)
	{	
		cout<<"\nEnter the quation "<< i+1;
		cout<<"\n Enter the value of a1 :";
		cin>>a[i];
		cout<<"\n Enter the value of b1 :";
		cin>>b[i];
		prod = prod * b[i];
	}
	for(i=0;i<n;i++)
	{
		m[i] = prod / b[i];
		m_inv[i] = calc_inv(m[i],b[i]);
		sum = sum + (a[i] * m[i] * m_inv[i]);
	}
	cout<<"The number is :" << (sum % prod);
}

==========OUTPUT===================
Enter the numer of equations3

Enter the quation 1
 Enter the value of a1 :2

 Enter the value of b1 :3

Enter the quation 2
 Enter the value of a1 :3

 Enter the value of b1 :5

Enter the quation 3
 Enter the value of a1 :2

 Enter the value of b1 :7
The number is :23
