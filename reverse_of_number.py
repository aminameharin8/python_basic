# Program to revers a given number
n=int(input("Enter the number to be reversed: "))
rev=0

while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
    
print("Reverse of the given number is: ",rev)
