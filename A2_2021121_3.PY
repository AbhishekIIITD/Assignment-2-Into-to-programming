from unicodedata import decimal


def radixconvertor(fr,to,n):
    dec=0
    multiplier=fr**0
    value={}
    for i in range(0,10):
        value[str(i)]=i
    for i in range(10,36):
        value[chr(i+55)]=i
    
    length=len(n)-1
    while(length>=0):
        if(value[n[length]]>fr):
            return "wrong input"
        dec=dec+value[n[length]]*multiplier
        multiplier*=fr
        length-=1
    x=""
    for i in range(10,36):
        value[str(i)]=chr(i+55)
    while(dec>0):
        x=str(value[str(int(dec)%to)])+x
        dec=dec//to
    return x


def decimal_binary(operation,decimal=0,binary=0):
    if operation==1:
        binary=radixconvertor(10,2,decimal)
        return binary
    elif operation==2:
        decimal=radixconvertor(2,10,binary)
        return decimal
    else:
        return "wrong input"

def hexadecimal_decimal(operation,decimal=0,hexadecimal=0):
    if operation==1:
        decimal=radixconvertor(16,10,hexadecimal)
        return decimal
    elif operation==2:
        hexadecimal=radixconvertor(10,16,decimal)
        return hexadecimal
    else:
        return "wrong input"

def octal_decimal(operation,decimal=0,octal=0):
    if operation==1:
        octal=radixconvertor(10,8,decimal)
        return octal
    elif operation==2:
        decimal=radixconvertor(8,10,octal)
        return decimal
    else:
        return "wrong input"


def binary_hexadecimal(operation,binary=0,hexadecimal=0):
    if operation==1:
        binary=radixconvertor(16,2,hexadecimal)
        return binary
    elif operation==2:
        hexadecimal=radixconvertor(2,16,binary)
        return hexadecimal
    else:
        return "wrong input"


def binary_octal(operation,binary=0,octal=0):
    if operation==1:
        binary=radixconvertor(8,2,octal)
        return binary
    elif operation==2:
        octal=radixconvertor(2,8,binary)
        return octal
    else:
        return "wrong input"

def hexadecimal_octal(operation,hexadecimal=0,octal=0):
    if operation==1:
        octal=radixconvertor(16,8,hexadecimal)
        return octal
    elif operation==2:
        hexadecimal=radixconvertor(8,16,octal)
        return hexadecimal
    else:
        return "wrong input"

    

print("1. Convert decimal to binary and vice-versa\n2. Convert decimal to hexadecimal and vice-versa \n3. Convert decimal to octal and vice-versa. \n4. Convert binary to hexadecimal and vice-versa. \n5. Convert binary to octal and vice-versa. \n6. Convert hexadecimal to octal and vice-versa. \n7. Convert number with radix A to radix B. Here A,B <= 36. ")

choice=int(input('Enter your choice : '))
while(choice>0 and choice<8):
    if(choice==1):
        print("Choose the operation\n1. Decimal to binary\n2. Binary to Decimal")
        choice=int(input())
        num=input("enter the number : ")
        if(choice==1):
            print(decimal_binary(choice,decimal=num))
        else:
            print(decimal_binary(choice,binary=num))
            

        
    elif(choice==2):
        print("Choose the operation\n1. hexadecimal to decimal\n2. decimal to hexadecimal")
        choice=int(input())
        num=input("enter the number : ")
        if(choice==1):
            print(hexadecimal_decimal(choice,hexadecimal=num))
        else:
            print(hexadecimal_decimal(choice,decimal=num))

    elif(choice==3):
        print("Choose the operation\n1. Decimal to octal\n2. octal to Decimal")
        choice=int(input())
        num=input("enter the number : ")
        if(choice==1):
            print(octal_decimal(choice,decimal=num))
        else:
            print(octal_decimal(choice,octal=num))

    elif(choice==4):
        print("Choose the operation\n1. hexadecimal to binary\n2. Binary to hexadecimal")
        choice=int(input())
        num=input("enter the number : ")
        if(choice==1):
            print(binary_hexadecimal(choice,hexadecimal=num))
        else:
            print(binary_hexadecimal(choice,binary=num))

    elif(choice==5):
        print("Choose the operation\n1. octal to binary\n2. Binary to octal")
        choice=int(input())
        num=input("enter the number : ")
        if(choice==1):
            print(binary_octal(choice,octal=num))
        else:
            print(binary_octal(choice,binary=num))

    elif(choice==6):
        print("Choose the operation\n1. hexadecimal to octal\n2. octal to hexadecimal")
        choice=int(input())
        num=input("enter the number : ")
        if(choice==1):
            print(hexadecimal_octal(choice,hexadecimal=num))
        else:
            print(hexadecimal_octal(choice,octal=num))

    elif(choice==7):
        
        radixA=int(input("Enter the radix A :"))
        radixB=int(input("Enter the radix B :"))

        num=input("enter the number : ")
        print(radixconvertor(radixA,radixB,num))
    else:
        print("Wrong input ")
    choice=int(input('Enter your choice : '))