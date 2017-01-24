#import some libraries
import math

print("Solve 2'th equation");

#input parameters
a = input("a = ");
b = input("b = ");
c = input("c = ");

#solve equation
if (b*b < 4*a*c):
	print("Pt vo nghiem");
else:
	delta = math.sqrt(b*b - 4*a*c);
	if delta == 0:
		x1 = (-b)/(2*a);
		x2 = x1;
		#Print x1, x2
		print(x1);
		print(x2);
	else:
		x1 = (-b + delta)/(2*a);
		x2 = (-b - delta)/(2*a);
		#Print x1, x2
		print "x1 =", x1
		print "x2 =", x2
