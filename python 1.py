def isIn(x, y):
    if len(x) <= len(y):
        if x.find(y) > 0:
            return True
    else:
        if x.find(y) > 0:
            return True
    return False
string = input('Enter frist String \n')
string2= input('Enter 2nd String \n')
print('Fisrt String :- ',string)
print('Second String :- ',string2)
print ('Result is :- ',format(isIn(string, string2)))



