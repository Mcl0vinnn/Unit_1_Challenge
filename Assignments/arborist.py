 # Arborist Tree Assignment
# SOH CAH TOA
import math

try:
    friend = 1.65
    x = int(input('What is the angle: '))
    x = math.degrees (x * 0.75)
    
    tree = math.tan (x * 1.65)
    
    print ('This is the intital height of the tree', tree)
except (ZeroDivisionError,ValueError):
    print ('that is not an answer')
    print ('please enter your actual answer')