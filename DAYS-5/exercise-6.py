# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz

for i in range(1, 101):
    if i % 3 ==0 and i% 5==0:
        print('FizzBuzz')
    elif i%3 ==0:
        print('Fizz')    
    elif i%5 ==0:
        print('Buzz')
    else:
        print(i)        