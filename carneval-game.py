from random import shuffle

l=['','O','']

def shuffler(l):
    shuffle(l)
    return l

def enter():
    num=int(input("Pick '0', '1', '2': "))
    if num in [0,1,2]:
        checker(num,l)
        return
    print('Choose a valid number:')
    enter()

def checker(num,l):
    if l[num]=='O':
        print('You guessed it right!')
        print(f'the list is {l} and ur guess is {num}')
        return
    else:
        print('Wrong Guess')
        print(f'the list is {l} and ur guess is {num}')
        shuffler(l)
        enter()
    

enter()
