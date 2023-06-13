import os
import sys
import time

def arrow_up(size):
	os.system("cls")
	for x in range(size):
		star=2*x+1
		space=3*size-x
		print(" "+"  "*(space) + " *"*star)
	
	for y in range(size):
		print(" "+" "*(size*6) +" *" )
	
def arrow_right(size):
	os.system("cls")
	print("\n"*(size-1))
	for x in range(size):
		if(x==(size-1)):
			print(" "*6*size+" *"*size + " *"*(x+1))
		else:
			print(" "*(8*size) + " *"*(x+1))
			
		
	for y in range(size):
		print(" "*(8*size) +" *"*(size-1-y))
        
def arrow_left(size):
	os.system("cls")
	print("\n"*(size-1))
	for x in range(size):
		if(x==(size-1)):
			print("  "+" "*2*size+" *"*size + " *"*(x+1))
		else:
			print("  "+" "*(2*size) + "  "*(size-x-1) +   " *"*(x+1))
			
		
	for y in range(size):
		print("  "+" "*(2*size)+"  "*(y+1) +" *"*(size-1-y))

def arrow_down(size):
	os.system("cls")
	print("\n"*2*(size-1))
	for y in range(size):
		print(" "+" "*(size*6) + " *")
        
	for x in range((size-1),-1,-1):
		star=2*x+1
		space=3*size-x
		print(" "+"  "*(space) + " *"*star)

def clockwise(size):
    arrow_up(size)
    time.sleep(0.5)
    arrow_right(size)
    time.sleep(0.5)
    arrow_down(size)
    time.sleep(0.5)
    arrow_left(size)
    time.sleep(0.5)

def anticlockwise(size):
    arrow_up(size)
    time.sleep(0.5)
    arrow_left(size)
    time.sleep(0.5)
    arrow_down(size)
    time.sleep(0.5)
    arrow_right(size)
    time.sleep(0.5)

print("Welcome to the arrow animation")
print("Enter desired rotation direction:")
print("1)clockwise  2)anticlockwise")
x=int(input())
size=int(input("Please enter the arrow size\n"))

while True:
    if x == 1:
        clockwise(size)
    elif x == 2:
        anticlockwise(size)