from os import replace
from os import system
system("clear")
print("""
 _______  _______  __   __  _______              ____         _______ 
|       ||       ||  |_|  ||       |            |    |       |  _    |
|_     _||    ___||       ||_     _|   ____      |   |       | | |   |
  |   |  |   |___ |       |  |   |    |____|     |   |       | | |   |
  |   |  |    ___| |     |   |   |               |   |  ___  | |_|   |
  |   |  |   |___ |   _   |  |   |               |   | |_  | |       |
  |___|  |_______||__| |__|  |___|               |___|   |_| |_______|
  \033[0;31m
                 _____________________
                |                     |
                |                     |
                |  \033[3;34m @alhassanAlharb7 \033[0;31m |
                |  \033[3;34m @F14Commander  \033[0;31m   |
                |                     |
                |_____________________|
""")
while True:
    print(""" \033[0;34m
from EN to 1,0 (1)
from 1,0 to EN (2)
Exit (X)
""")
    User = input(">> \033[0;38m")
    if User == "1":
        Text =input("Text >> ")
        print("")
        a=Text.replace("a","01100001 ")
        b=a.replace("b","01100010 ")
        c=b.replace("c","01100011 ")
        d=c.replace("d",'01100100 ')
        e=d.replace("e","01100101 ")
        f=e.replace("f",'01100110 ')
        g=f.replace("g",'01100111 ')
        h=g.replace("h",'01101000 ')
        i=h.replace("i",'01101001 ')
        j=i.replace('j','01101010 ')
        k=j.replace("k",'01101011 ')
        l=k.replace("l",'01101100 ')
        m=l.replace("m",'01101101 ')
        n=m.replace("n",'01101110 ')
        o=n.replace("o",'01101111 ')
        p=o.replace('p','01110000 ')
        q=p.replace('q','01110001 ')
        r=q.replace('r','01110010 ')
        s=r.replace("s",'01110011 ')
        t=s.replace('t','01110100 ')
        u=t.replace('u','01110101 ')
        v=u.replace('v','01110110 ')
        w=v.replace('w','01110111 ')
        x=w.replace('x','01111000 ')
        y=x.replace('y','01111001 ')
        z=y.replace('z','01111010 ')
        space=z.replace('00100000',' ')
        print(space)
    elif User =="2":
        Text =input("Text >> ")
        print("")
        space=Text.replace('00100000',' ')
        a=Text.replace("01100001 ",'a')
        b=a.replace("01100010 ","b")
        c=b.replace("01100011 ","c")
        d=c.replace("01100100 ",'d')
        e=d.replace("01100101 ","e")
        f=e.replace("01100110 ",'f')
        g=f.replace("01100111 ",'g')
        h=g.replace("01101000 ",'h')
        i=h.replace("01101001 ",'i')
        j=i.replace('01101010 ','j')
        k=j.replace("01101011 ",'k')
        l=k.replace("01101100 ",'l')
        m=l.replace("01101101 ",'m')
        n=m.replace("01101110 ",'n')
        o=n.replace("01101111 ",'o')
        p=o.replace('01110000 ','p')
        q=p.replace('01110001 ','q')
        r=q.replace('01110010 ','r')
        s=r.replace("01110011 ",'s')    
        t=s.replace('01110100 ','t')
        u=t.replace('01110101 ','u')
        v=u.replace('01110110 ','v')
        w=v.replace('01110111 ','w')
        x=w.replace('01111000 ','x')
        y=x.replace('01111001 ','y')
        z=y.replace('01111010 ','z')
        #_________
        a=z.replace("01100001",'a')
        b=a.replace("01100010","b")
        c=b.replace("01100011","c")
        d=c.replace("01100100",'d')
        e=d.replace("01100101","e")
        f=e.replace("01100110",'f')
        g=f.replace("01100111",'g')
        h=g.replace("01101000",'h')
        i=h.replace("01101001",'i')
        j=i.replace('01101010','j')
        k=j.replace("01101011",'k')
        l=k.replace("01101100",'l')
        m=l.replace("01101101",'m')
        n=m.replace("01101110",'n')
        o=n.replace("01101111",'o')
        p=o.replace('01110000','p')
        q=p.replace('01110001','q')
        r=q.replace('01110010','r')
        s=r.replace("01110011",'s')
        t=s.replace('01110100','t')
        u=t.replace('01110101','u')
        v=u.replace('01110110','v')
        w=v.replace('01110111','w')
        x=w.replace('01111000','x')
        y=x.replace('01111001','y')
        z=y.replace('01111010','z')
        print(z)
    elif User =="x" or User == "X" or User == "exit" or User =="Exit" or User == "EXIT":
        exit("See You agen")
    else:
        print("Error.")
