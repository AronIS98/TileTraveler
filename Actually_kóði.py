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
