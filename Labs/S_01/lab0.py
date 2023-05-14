#Simple tutorial for Python String Methods,{ strip(), swapcase(), title() }
#Author: Muhammad Alkahwagy

strip_desc = '''
***strip() method***

Definition and Usage:
The strip() method removes any leading (spaces at the beginning)
and trailing (spaces at the end) characters (space is the default leading character to remove)

Syntax:
string.strip(characters)

Example: Remove the leading and trailing characters:

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)

Output:'''

swapcase_desc = '''
***swapcase() method***

Definition and Usage:
The swapcase() method returns a string where all the upper case letters are lower case and vice versa.

Syntax
string.swapcase()

Example: Make the lower case letters upper case and the upper case letters lower case:

txt = "Hello My Name Is Alaa"
x = txt.swapcase()
print(x)

Output:'''

title_desc = '''
***title() method***

Definition and Usage
The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
If the word contains a number or a symbol, the first letter after that will be converted to upper case.

Syntax
string.title()

Example: Make the first letter in each word upper case:

txt = "welcome to my python program"
x = txt.title()
print(x)

Output:
'''
print("\nWelcome to Python String Methods tutorial")

while True:
    print("Enter method's number for more details!")
    choice = input("1.strip()    2.swapcase()    3.title()  ESC.exit\n")
    if(choice):
        if choice == '1':
            print(strip_desc)
            txt = ",,,,,rrttgg.....banana....rrr"
            x = txt.strip(",.grt")
            print(x+'\n')
        elif choice == '2':
            print(swapcase_desc)
            txt = "Hello My Name Is Alaa"
            x = txt.swapcase()
            print(x+'\n')
        elif choice == '3':
            print(title_desc)
            txt = "welcome to my python program"
            x = txt.title()
            print(x+'\n')
        elif choice == '0':
            print("See ya!")
            break
        else:
            print("Invalid Choice!")