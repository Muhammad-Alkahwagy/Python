#prompt the user to enter his name
MyName = input("Hello, please enter your name: ")
#prompt the user to enter his age
MyAge = input("Please enter your age: ")
#prompt the user to enter his faculty
MyFaculty = input("Please enter your faculty: ")


f1 = open("Personal_Info.txt", "w")
f1.write("Good evening!\n")
f1.write("This is "+MyName+'\n')
f1.write("I'm %s years old\n" %MyAge)
f1.write("I studied at %s \n" %MyFaculty)
f1.write("Nice to meet ya!\n")
f1 = open("Personal_Info.txt","r")
print(f1.read())
f1.close()