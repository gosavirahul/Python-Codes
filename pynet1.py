def isIn(x, y):
    if len(x) <= len(y):
        if x.find(y) > 0:
            return True
    else:
        if x.find(y) > 0:
            return True
    return False

str1 = input('Enter first string: ')
str2 = input('Enter second string: ')

print ('Either string occurs anywhere in the other? {}'.format(isIn(str1, str2)))
