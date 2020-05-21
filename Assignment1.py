#WAP that ask user to enter their name and their age.print out a message address to them that tells them the year they will turn 100 years old


try:
    
    name = str(input("please enter your name:" ))
    age  = int(input("Please enter your age: "))
    num = 100-age
    if age >=100:
        
        print(name, "you are already 100 years old. Your age is", age)
    else:
        print(name, "you will turn 100 years old after", num, "years")

except ValueError:
    print("invalid name or age \n please try again \n ")
    
    name = str(input("please enter your name again: "))
    age = int(input("please enter your age again: "))

    if age>=100:
        print(name, "your are already 100 years old. your age is", age)

    else:
        print(name, "you will turn 100 years old after", age, "years")
