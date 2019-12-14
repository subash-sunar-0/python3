#!/usr/bin/python3

import random

r = random.randint(0,9)

run = True
while run:
    num = int(input("guss any number between 0-9: "))

    if num < r:
        print("Too Low!!")
        
    
    elif num > r:
        print("Too High!!")
           

    elif num > 9:
        print("Invalid number")
        num = int(input("Enter  any number again between 0-9: "))
           

    
    elif num == r:
        print("You Won!!!") 

        a = str(input("Do you want to play again 'y/n': "))
        if a == 'y':
            num = int(input("Enter any number between 0-9: "))

            
        elif a =='n':
            print("bye bye!!!!")
            run = False
            
            
        else:
            print("Enter 'y/n'")
            a = str(input("Do you want to play again 'y/n': "))
                
            


            
            
            
    

        