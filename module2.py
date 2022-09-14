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


names = ["Janet", "Betty"]

test= []
exams = []

for name in names:
    t = int(input(f"Enter {name}'s Test Score: "))
    e = int(input(f"Enter {name}'s Exam Score: "))

    test.append(t)
    exams.append(e)

print(test, exams)