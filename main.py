
#Trangle


# sum = int(input("enter the number of rows, again"))    # short cut for emoji list in windows 10 - windows+:
# for i in range(1,sum + 1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()



# #Triangle2
#
# num = int(input("enter the num of rows"))
# x = 1
# for i in range(1,num+1):
#     for j in range(1,x + 1):
#         print("💖", end=" ")
#     x = x+2
#     print()
# # sum = int(input("jedan br."))
# x = 1
# for i in range(1,num +1):
#     for j in range(1, x+1):
#         print("💕", end=" ")
#     x = x+3
#     print()
#
# for i in range(0, num):
#     for j in range(0, num-i+1):
#         print(end=" ")
#     for j in range(1,i +1):
#         print("🤳",end=" ")
#     print()
#





# num = int(input("How many?"))
# for i in range(0, num):
#     for j in range(0, num -i-1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("💕 ", end=" ")
#     print()

# numbers in pyramid shape
# num = int(input("enter the number of rows"))
# for i in range(1,num +1):
#     for j in range(1, num -i+1):
#         print(end=" ")
#     for j in range(i,0,-1):
#         print(j, end="")
#     for j in range(2, i + 1):
#         print(j, end="")
#     print()

#numbers in square shape
# num = int(input("what is the number of rows:"))
# n_list = [[0 for x in range(num)] for y in range(num)]#nested list using list comprehension method, and we had 2D
#                                                    #n_list[row value][column value]
# n=1
# low = 0
# high = num-1
# count = int((num+1)/2)
# for i in range(count):
#     for j in range(low,high + 1):
#         n_list[i][j]=n
#         n=n+1
#     for j in range(low+1,high+1):
#         n_list[j][high]=n
#         n=n+1
#     for j in range(high -1,low-1,-1):
#         n_list[high][j]=n
#         n=n+1
#     for j in range(high-1,low,   -1):
#         n_list[j][low]=n
#         n=n+1
#     low=low+1
#     high=high-1
#
# for i in range(num):
#     for j in range(num):
#         print(n_list[i][j],end="\t")
#     print()


# num = int(input("enter the num. of rows"))
# for i in range(0,num):
#     for j in range(0,num-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("💖",end=" ")
#     print()
#
# #Triangle upside down
# num = int(input("enter the num. of rows"))
# for i in range(num,0,-1):
#     for j in range(0,num-i):
#         print(end=" ")
#     for j in range(0,i):
#         print("*", end=' ')
#     print()
#
# #LETTER D
# for row in range(7):
#     for col in range(5):
#         if (col)==0 or (col==4 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
# for row in range(7):
#     for col in range(5):
#         if (col)==0 or (col==4 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()







# #LETTER A

# for row in range(7):
#     for col in range(5):
#         if ((row==0 or row==3 or row==6) and (col>0 and col<4)) or (col==0 and (row>0 and row<3)) or (col==4 and (row>3 and row<6)):
#             print("💖", end="")
#         else:
#             print(" ")
#     print()

# for row in range(7):
#     for col in range(5):
#         if ((col==0 or col==4) and row !=0) or ((row==0 or row==3 and (col>0 and col<4))):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
#
# #ZERO
# for row in range(7):
#     for col in range(5):
#         if ((col==0 or col==4) and row !=0) or ((row==0 or row==6 and (col>0 and col<4))):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
#
# #HEART
#
# for row in range(6):
#     for col in range(7):
#         if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
#             print("*", end="")
#         else:
#             print(" ",end="")
#     print()
#
# #LETTER Y

# for row in range(7):
#     for col in range(8):
#         if (row+col==7) or (row==0 and col==1) or (row==1 and col==2) or (row==2 and col==3):
#             print("*",end="")
#         else:
#             print(" ",end="")
 #   print()
#
# #LETTER Z
#
for row in range(5):
    for col in range(5):
        if (row+col==4) or (row==0) or (row==4):
            print("*", end="")
        else:
            print(" ",end="")
    print()
#
#DIAMOND SHAPE

# def pyramid(rows):
#     for i in range(rows):
#         print(''*(rows-i-1)+'*'*(i+1))
#     # for j in range (rows-1,0,-1):
#     #     print(''*(rows-j)+'*'*(j))
# print(pyramid(5))

