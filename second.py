for row in range(7):
    for col in range(8):
        if (row+col==7) or (row==0 and col==1) or (row==1 and col==2) or (row==2 and col==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()

