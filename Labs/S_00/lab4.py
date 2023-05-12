#prompt for sensor 1 reading
s1= int(input("Enter value of sensor 1: "))

#prompt for sensor 2 reading
s2= int(input("Enter value of sensor 2: "))

#prompt for sensor 3 reading
s3= int(input("Enter value of sensor 3: "))

#Insert readings in a list
MyList = [s1,s2,s3]

#Insert readings in a tuple
MyTuple = (s1,s2,s3)

#Insert readings in a dictionary
MyDict = {
    "Reading1": s1,
    "Reading2": s2,
    "Reading3": s3
}

#print readings
print('\n')
print(MyList)
print(MyTuple)
print(MyDict)