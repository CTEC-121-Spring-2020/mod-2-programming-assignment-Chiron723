"""
CTEC 121
<Stephen Guild>
<MOD 2 Programming Assignment>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
import math
def main():
    
    #1. Demonstrate assignment statements
    # a. create several variables and assign them values. 
    myint=5
    afloat=4.5
    zastring="The examples of int and float are:"
    print(zastring,myint,"and",afloat)
    print()

    #2. Demonstrate the use of the end and sep keywords in print statements.
    print("Spider","Man",sep="-",end="!")
    print("\n")

    #3. Demonstrate the use of the tab, quote and backslash escape characters.
    print("Batman\\Superman","\t" "World's finest\"",)
    print()

    #4. Demonstrate getting input from the user.
    movieString=input("please enter favorite series: ")
    print(movieString)
    myint=int(input("Enter a whole number: "))
    print(myint)
    #string invalid, float number invalid
    myfloat=float(input("enter a decible number: "))
    print(myfloat)
    #string invalid
    myeval=eval(input("Enter a number or a numeric expressions:"))
    print(myeval)
    #string invalid
    print()

    #5. Demonstrate simultaneous assignment
    a,b=5,6
    print(a,b)
    c,d=eval(input("enter two numbers sepparated by a comma:"))
    print(c,d)
    print()

    #6. Demonstrate integer arithmetic
    #output the quotient of five divided by two.
    print(int(5//2))
    #output the remainder of five divided by two.
    print(float(5/2))
    print()
    
    #7. Demonstrate definite loops
    for i in (1,2,3,4,5):
        print(i)
    print()
    for i in range(5):
        print(i)
    print()
    for i in range(11,23,3):
        print(i)
    print()
    
    #8. Demonstrate the use of math library
    print(math.pi)
    print(math.sqrt(16))
    print(math.ceil(1.7))
    print(math.floor(1.7))
    print(math.sqrt(1.2+1.6))
    print((3+5)**3)
    print()
    
    #9. Demonstrate the accumulator pattern by getting five values from the user and calculating the sum of the values and the sum of squares.
    sum=0
    i=0
    v,w,x,y,z=eval(input("put numbers here... "))
    for p in(v,w,x,y,z):
        sum=sum+p
    print(sum)
    square=i+math.sqrt(p)*2
    print(square)
    print()





main()