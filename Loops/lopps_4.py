name = input ('Please enter a name: ')

while name:
    name = input ('Please enter a name: ')
    print (name ,'has been invited!')
    print ('Who else do you want to invite?')
    name +=1
    if name == 'end':
        break
    

print ('This is the total amount of people you invited: ', name)
