# count to 100, if the number is divisable by three let the computer say fizz instead of 3
#if the number is divisable by five let the computer say buzz instead of 5
#every other number should be said so if the number is 1 then it should say 1
#if the number is divisable by both 3 and 5 the computer should say fizzbuzz

for num in range(1 ,101):

 if num%3+num%5==0:   #num%3 == 0 and num%5==0
    print ("fizzbuzz")
 elif num%3==0:
    print ("fizz")
 elif num%5==0:
    print ("buzz")

 else:
    print (num)