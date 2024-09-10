# MAKE 10 LESS THAN OR GREATER THAN

x = int(input('Choose any number: '))


if 10 > x:
    print ('This number is less than ' , 10)
    print ('you must like the number 10')
elif 10 < x:
    print ('This number is greater than ' , 10)
    print ('this is the amount of cash you have now' , x)
else:
    print ('that number is EQUAL to 10' , x)
    print ('you must hate other numbers')