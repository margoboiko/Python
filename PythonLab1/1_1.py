import math

x = float(input('Please enter x: '))
a = float(input('Please enter a: '))
e = float(input('Please enter e: '))

sum1 = 0
k = 0

sum2 = ((math.log((a + x))**(2*k))/(2**k + (math.factorial(k))))

print(sum2)

while(math.fabs(sum2) > e):
	sum1+=sum2
	sum2 = ((math.log((a + x))**(2*k))/(2**k + (math.factorial(k))))
	k=k+1

print('Sum = ', sum2, '\nk = ', k+1, end='\n\n')