

#Program that lets user enter a number until a negative number is entered


repeat= True
count= 0
lowest= -1
highest= -1

while repeat:
    num= int(input("Enter number (negative number to quit: "))

    if (num<0):
        repeat= False

    else:
        if (count == 0):
            lowest = num
            highest = num


        else:
        
            if (num < lowest):
                 lowest= num

            if (num > highest):
                 highest= num

    count= count+1

if (count==0):
    print("No number entered.")

else:
    print("The highest number is: " + str(highest))
    print("The lowest number is: " + str(lowest))
