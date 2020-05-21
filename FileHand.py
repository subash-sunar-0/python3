#!/usr/bin/python3

import os


#open a file 

fo = open('subash.txt', 'r+')

#read a file
str = fo.read(10)
print('read String is: ',str)

#check current position
position = fo.tell()
print('current file position: ', position)

#reposition pointer at the beginning once again
position=fo.seek(0,0)
str = fo.read(10)
print('Again read string is: ', str)



#writing on file
#fo.write("python is a greate language.\nYeah it\'s greate" )


#os.rename('test.txt', 'subash.txt')
os.remove('subash.txt')




#close opened file

fo.close()
