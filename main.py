# Assignment 1
# ICS3U
# Faraz
# March 28, 2018
             
def CtoF (temp):
    temp = round(32+(temp*1.8))
    return temp

def FtoC (temp):
    temp = round((0.55556)*(temp-32))
    return temp
repeat = 1
while repeat == 1:
    choice = int(input("Enter 1 for C to F, Enter 2 for F to C:"))
    a = int(input("Enter the temperature you would like to convert:"))
    while ( choice == 1 and a <= -273 ) or ( choice == 2 and a <= -459 ):
        print("The temperature you have entered is below absolute zero")
        break
    if choice == 1:
        print(CtoF(a))
    else:
        print(FtoC(a))
    rep = str(input("Would you like to make another conversion? (Y or N)"))
    if rep == "N":
        repeat = 0
