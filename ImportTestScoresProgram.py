#A program that allows the user to import files located on the user's computer
#The file contains test scores in which the program gives the average




def avg(numbers):
    average=(sum(numbers)/len(numbers))
    return average
numbers=[]


print("The numbers in the file are: ")
with open('C:\\Users\Jules\\Downloads\\Test_File.txt' , 'r') as lines:
    for line in lines:
        elements=line.split()
        print(line.rstrip('\n'))
        numbs=(float(element) for element in elements)
        numbers.extend(numbs)

print('The avergage is %s' % avg(numbers))
