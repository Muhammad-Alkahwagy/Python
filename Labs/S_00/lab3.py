#prompt the user to enter two numbers
n1= int(input("Enter number1: "))
n2= int(input("Enter number2: "))
print('\n')

#print the output of mathematical operations
print("Sum = %d"%(n1+n2))
print("Dif = %d"%(n1-n2))
print("Mul = %d"%(n1*n2))
print("Div = %d"%(n1/n2))
print("Mod = %d"%(n1%n2))
print("Exp = %d"%(n1**n2))
print('\n')

#print the output of bitwise operations
print("AND =  %d"%(n1&n2))
print("OR  =  %d"%(n1|n2))
print("XOR =  %d"%(n1^n2))
print("NOTn1 = %d"%(~n1))
print("NOTn2 = %d"%(~n2))
print("ShiftLeftN1  = %d"%(n1<<1))
print("ShiftLeftN2  = %d"%(n2<<1))
print("ShiftRightN1 = %d"%(n1>>1))
print("ShiftRightN2 = %d"%(n2>>1))
print('\n')

#print the output of relational operations
print("N1 is Greater than N2 = %s"%(n1>n2))
print("N1 is Less than N2   = %s"%(n1<n2))
print("N1 is equal to N2    = %s"%(n1==n2))
print("N1 is greater than or equal N2 = %s"%(n1>=n2))
print("N1 is less than or equal N2 = %s"%(n1<=n2))