n=True
s=True
w=True
e=True
xy=0.0

def allowed(xy)
if xy==1.1 or xy==2.1 or xy== 3.1 or xy==2.2 or xy==3.2 or xy==3.3:
    e=False
if xy==1.1 or xy ==2.1 or xy== 3.1 or xy==1.2 or xy==3.2 or xy==1.3:
    w=False
if xy==1.1 or xy==2.1 or xy==3.1 or xy==2.3:
    s=False
if xy== 1.3 or xy== 2.3 or xy== 3.3 or 2.2:
    n=False
return n, e, s, w

def step(position,command):
    '''Moves position in a 3x3 grid'''
    if command == 'n':
        position += 0.1
    elif command == 's':
        position -= 0.1
    elif command == 'e':
        position += 1.0
    elif command == 'w':
        position -= 1.0
    return position


def menu(n,s,e,w):
    instruction = 'You can travel:'

    if n and e and s:
        option = '{} (N)orth or (E)ast or (S)outh'.format(instruction)
    elif e and s:
        option = '{} (E)ast or (S)outh'.format(instruction)
    elif e and w:
        option = '{} (E)ast or (W)est'.format(instruction)
    
    elif s and w:
        option = '{} (S)outh or (W)est'.format(instruction)
    
    elif s and e:
        option = '{} (E)ast or (S)outh'.format(instruction)
    
    elif s:
        option = '{} (S)outh'.format(instruction)
    
    elif n:
        option = '{} (N)orth'.format(instruction)
    
    elif e:
        option = '{} (E)east'.format(instruction)
