
import math
import random

###################################
 # Part 1
###################################

def primary_school_quiz(flag, n):
    crt = 0
    if flag==0:
      for i in range(n):
         n1 = random.randint(0,9)
         n2 = random.randint(0,9)
         print("Question",i+1,": ")
         print("What is the result of",n2,"-",n1,"?",end = " ")
         answr = int(input())
         if answr==(n2-n1):
            crt = crt + 1
    elif flag==1:
      for i in range(n):
         n1 = random.randint(0,9)
         n2 = random.randint(0,9)
         print("Question",i+1,": ",n1,"*",n2,"=",end = " ")
         answr = int(input())
         if answr==(n1*n2):
            crt = crt + 1
    return(crt)


def high_school_eqsolver(a,b,c):
    print("The quadratic equation:",a,"·x^2 +",b,"·x +",c,"= 0")
    if(a==0 and b==0 and c==0):
        print("is satisfied for all numbers of x")
    elif(a==0 and b==0):
        print("is satisfied for no number of x")
    elif(a==0):
        print("has the following root/solution:",(-c/b))
    elif ((b**2-4*a*c) == 0):
        print("has only one solution, a real root:")
        print((-b+(b**2-4*a*c)**0.5)/(2*a))
    elif ((b**2-4*a*c) > 0):
        print("has the following real roots:")
        a1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
        a2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
        print(a1,"and",a2)
    elif ((b**2-a*a*c) <0):
        print("has the following two complex roots:")
        a1 = -b/(2*a)
        a1b = (abs(b**2-4*a*c))**0.5/(2*a)
        a2 = -b/(2*a)
        a2b = (abs(b**2-4*a*c))**0.5/(2*a)
        print((a1,"+ i",a1b),"\nand\n",(a2,"- i",a2b))
        

###################################
 # Part 2
###################################



print("**************************************************************")
print("*                                                            *")
print("*  __Welcome to my math quiz-generator / equation-solver__   *")
print("*                                                            *")
print("**************************************************************")

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")

if status=='1':
    print("*******************************************************************************")
    print("*                                                                             *")
    print("*  __",name,", welcome to my quiz-generator for primary school students.__    *")
    print("*                                                                             *")
    print("*******************************************************************************")
    print (name,end=" ")
    prac = int(input("What would you like to practice? Enter\n0 for Subtraction\n1 for multiplicationhhh\n"))
    amnt = int(input("How many practice questions would you like to do?"))
    print(name,"here are your ",amnt,"questions")
    mark = primary_school_quiz(prac,amnt)
    if (mark/amnt*100 >= 90):
       print("Congrats",name,"! You'll probably get an A tomorrow. Now go eat your dinner and go to sleep.")
    elif (mark/amnt*100 >= 70):
       print("You did well",name,", but I know you can do better.")
    else:
       print("I think you need some more practice",name,".")

elif status=='2':
    print("*************************************************************************")
    print("*                                                                       *")
    print("*    __quadratic equation, a·x^2 + b·x + c= 0, solver for ",name,"__    *")
    print("*                                                                       *")
    print("*************************************************************************")


    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        question = question.lower()

        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            a = int(input("Enter a number the coefficient a:"))
            b = int(input("Enter a number the coefficient b:"))
            c = int(input("Enter a number the coefficient c:"))
            high_school_eqsolver(a,b,c)
else:
    print(name,"you are not a target audience for this softwaree!")

print("Good bye "+name+"!")

