num = int(input("Enter a number: "))  
  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   # use while loop to iterate un till zero  
   while(num > 0):  
       sum += num  
       num -= 1  
   print("The sum is",sum)
   

# while loop

n = int(input("Enter Number to calculate sum"))

total_numbers = n
sum=0
while (n >= 0):
    sum += n
    n-=1
print ("sum using while loop ", sum)

   # sum of random number given by user

   n=int(input("How many numbers you want to input:"))
sum1=0
for i in range(0,n):
    num=int(input("Enter number:"))
    sum1+=num
print(sum1)

