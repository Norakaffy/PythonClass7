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


names = ["Janet", "Betty", "Serena", "Linda", "Anna"]

test= []
exams = []


for name in names:
    t = int(input(f"Enter {name}'s Test Score: "))
    e = int(input(f"Enter {name}'s Exam Score: "))


    test.append(t)
    exams.append(e)

totalscore = []

a = 0

totalscore.append(test[a] + exams[a])
a = a+1

print("==="*10)

b = 0

for student in names:
    if totalscore[b] <= 39 and totalscore[b]>= 0:
        print(f"{student} got an F")

    elif totalscore[b] <=49 and totalscore[b]>= 40:
        print(f"{student} got a E")


    elif totalscore[b] <=59 and totalscore[b]>= 50:
        print(f"{student} got a D")

    elif totalscore[b] <=69 and totalscore[b]>= 60:
        print(f"{student} got a C")

    elif totalscore[b] <=79 and totalscore[b]>= 70:
        print(f"{student} got a B")


    elif totalscore[b] <=100 and totalscore[b]>= 80:
        print(f"{student} got a A")

    else:
        print ("invalid score")


