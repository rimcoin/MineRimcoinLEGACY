from threading import Thread
import random,sys,os
c=[]
def getMoneyLook(n):
    i=str(n)
    try:
        j=i.index(".")
        i=i[:i.index(".")+7]
    except:
        i+=".000000"
        j=-1
    if j==-1:
        return i
    else:
        i+="0"*(6-((len(i)-1)-j))
    return i;
def rcm(i):
    j=0
    k=0
    while j<(i**0.01):
        try:
            k+=int(j%int(j**0.5))
        except:
            pass
        j+=1
    return (k%2**16)==0;
def mine():
    global c
    j=0
    mn=0
    while True:
        try:
            go=random.randint(10**5,(10**6)-1)
            if rcm(go):
                c.append(str(go))
                mn+=1
        except:
            pass
        j+=1
        if mn%256==0:
            os.system("curl http://rimcoin.pythonanywhere.com/sub:"+sys.argv[1]+":"+"/".join(c)+" &")
            c=[]
threads=4
while threads>=0:
    Thread(target=mine).start()
    threads-=1
