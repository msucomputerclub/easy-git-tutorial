def ftToIn(ft):
    ft *= 12
    return ft

def inToFt(inch):
    inch //=12
    return inch

i = 0

while(i != 1):
    m = int(input("Enter 0 for ft to inches OR Enter 1 for in to ft: "))
    print()

    if(m==0):
        feet = int(input("Enter number in feet: "))
        print()
        print(ftToIn(feet))
        print()
    elif(m==1):
        inch = int(input("Enter number in inches: "))
        print()
        print(inToFt(inch))
        print()
    else:
        print("invalid input. Enter a number between 0-1")
        print()
    
