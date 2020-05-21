#Python Program to Convert Decimal to Binary, Octal and Hexadecimal

num = int(input("Enter the number: "))


#choice=int(input("convert number into: \n1.Binary\n2.Octal\n3.Hexadecimal\n"))

run =True
while run:
    choice=int(input("convert number into: \n1.Binary\n2.Octal\n3.Hexadecimal\n"))


    if choice==1:
        print("The Binary value of ",num, "is", bin(num))
        run = False

    elif choice ==2:
        print("The octal valu of ",num, "is", oct(num))
        run = False

    elif choice==3:
        print("The Hexadecimal value of", num, "is", hex(num))
        run = False

    else:
        print("please Enter correct choice")
        num = int(input("Enter the number: "))
       # choice=int(input("convert number into: \n1.Binary\n2.Octal\n3.Hexadecimal\n"))



