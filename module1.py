#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kafonya Nora
#
# Created:     19/07/2021
# Copyright:   (c) Kafonya Nora 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()



for i in range(0,10,2):
    print(i)

names=[]

for i in range (1,6):
    names=[]
    name = input(f"Enter your name {i}: ")
    names.append(name)


#print(names)

print("=" * 50)


for na in names:
    print(na)