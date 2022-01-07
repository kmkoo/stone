from tkinter import *
from random import *

per = [75, 65, 55, 45, 35, 25]
percent = per[0]
acl = 0
bcl = 0
ccl = 0
ac = 0
bc = 0
cc = 0
tot = 0

def ran(perc):
    global torf
    p = randint(1, 100)
    if p < perc:
        torf = True
    else:
        torf = False


def per_changer():
    global per, percent, torf
    ran(percent)
    if torf:
        if percent == per[0]:
            percent = per[1]
        elif percent == per[1]:
            percent = per[2]
        elif percent == per[2]:
            percent = per[3]
        elif percent == per[3]:
            percent = per[4]
        elif percent == per[4]:
            percent = per[5]
        elif percent == per[5]:
            percent = per[5]
    elif not torf:
        if percent == per[0]:
            percent = per[0]
        elif percent == per[1]:
            percent = per[0]
        elif percent == per[2]:
            percent = per[1]
        elif percent == per[3]:
            percent = per[2]
        elif percent == per[4]:
            percent = per[3]
        elif percent == per[5]:
            percent = per[4]

    suc.configure(text="성공 확률 "+ str(percent) + "%")
    fai.configure(text="성공 확률 "+ str(percent) + "%")


def aclicked():
    global torf, acl, ac, tot
    if acl == 10:
        return
    acl += 1
    per_changer()
    if acl == 1:
        if torf:
            a1.configure(text="◆")
            ac += 1
            tot += 1
        elif not torf:
            a1.configure(text="◆", fg="gray")
    if acl == 2:
        if torf:
            a2.configure(text="◆")
            ac += 1
            tot += 1
        elif not torf:
            a2.configure(text="◆", fg="gray")
    if acl == 3:
        if torf:
            a3.configure(text="◆")
            ac += 1
            tot += 1
        elif not torf:
            a3.configure(text="◆", fg="gray")
    if acl == 4:
        if torf:
            a4.configure(text="◆")
            ac += 1
            tot += 1
        elif not torf:
            a4.configure(text="◆", fg="gray")
    if acl == 5:
        if torf:
            a5.configure(text="◆")
            ac += 1
            tot += 1
        elif not torf:
            a5.configure(text="◆", fg="gray")
    if acl == 6:
        if torf:
            a6.configure(text="◆")
            ac += 1
            tot += 1
        elif not torf:
            a6.configure(text="◆", fg="gray")
    if acl == 7:
        if torf:
            a7.configure(text="◆")
            ac += 1
            tot += 1
        elif not torf:
            a7.configure(text="◆", fg="gray")
    if acl == 8:
        if torf:
            a8.configure(text="◆")
            ac += 1
            tot += 1
        elif not torf:
            a8.configure(text="◆", fg="gray")
    if acl == 9:
        if torf:
            a9.configure(text="◆")
            ac += 1
            tot += 1
        elif not torf:
            a9.configure(text="◆", fg="gray")
    if acl == 10:
        if torf:
            a10.configure(text="◆")
            ac += 1
            tot += 1
        elif not torf:
            a10.configure(text="◆", fg="gray")
    acount.config(text=str(ac))
    total.configure(text="세공 성공 총 " + str(tot) + "회")

def bclicked():
    global torf, bcl, bc, tot
    if bcl == 10:
        return
    bcl += 1
    per_changer()
    if bcl == 1:
        if torf:
            b1.configure(text="◆")
            bc += 1
            tot += 1
        elif not torf:
            b1.configure(text="◆", fg="gray")
    if bcl == 2:
        if torf:
            b2.configure(text="◆")
            bc += 1
            tot += 1
        elif not torf:
            b2.configure(text="◆", fg="gray")
    if bcl == 3:
        if torf:
            b3.configure(text="◆")
            bc += 1
            tot += 1
        elif not torf:
            b3.configure(text="◆", fg="gray")
    if bcl == 4:
        if torf:
            b4.configure(text="◆")
            bc += 1
            tot += 1
        elif not torf:
            b4.configure(text="◆", fg="gray")
    if bcl == 5:
        if torf:
            b5.configure(text="◆")
            bc += 1
            tot += 1
        elif not torf:
            b5.configure(text="◆", fg="gray")
    if bcl == 6:
        if torf:
            b6.configure(text="◆")
            bc += 1
            tot += 1
        elif not torf:
            b6.configure(text="◆", fg="gray")
    if bcl == 7:
        if torf:
            b7.configure(text="◆")
            bc += 1
            tot += 1
        elif not torf:
            b7.configure(text="◆", fg="gray")
    if bcl == 8:
        if torf:
            b8.configure(text="◆")
            bc += 1
            tot += 1
        elif not torf:
            b8.configure(text="◆", fg="gray")
    if bcl == 9:
        if torf:
            b9.configure(text="◆")
            bc += 1
            tot += 1
        elif not torf:
            b9.configure(text="◆", fg="gray")
    if bcl == 10:
        if torf:
            b10.configure(text="◆")
            bc += 1
            tot += 1
        elif not torf:
            b10.configure(text="◆", fg="gray")
    bcount.config(text=str(bc))
    total.configure(text="세공 성공 총 " + str(tot) + "회")

def cclicked():
    global torf, ccl, cc
    if ccl == 10:
        return
    ccl += 1
    per_changer()
    if ccl == 1:
        if torf:
            c1.configure(text="◆")
            cc += 1
        elif not torf:
            c1.configure(text="◆", fg="gray")
    if ccl == 2:
        if torf:
            c2.configure(text="◆")
            cc += 1
        elif not torf:
            c2.configure(text="◆", fg="gray")
    if ccl == 3:
        if torf:
            c3.configure(text="◆")
            cc += 1
        elif not torf:
            c3.configure(text="◆", fg="gray")
    if ccl == 4:
        if torf:
            c4.configure(text="◆")
            cc += 1
        elif not torf:
            c4.configure(text="◆", fg="gray")
    if ccl == 5:
        if torf:
            c5.configure(text="◆")
            cc += 1
        elif not torf:
            c5.configure(text="◆", fg="gray")
    if ccl == 6:
        if torf:
            c6.configure(text="◆")
            cc += 1
        elif not torf:
            c6.configure(text="◆", fg="gray")
    if ccl == 7:
        if torf:
            c7.configure(text="◆")
            cc += 1
        elif not torf:
            c7.configure(text="◆", fg="gray")
    if ccl == 8:
        if torf:
            c8.configure(text="◆")
            cc += 1
        elif not torf:
            c8.configure(text="◆", fg="gray")
    if ccl == 9:
        if torf:
            c9.configure(text="◆")
            cc += 1
        elif not torf:
            c9.configure(text="◆", fg="gray")
    if ccl == 10:
        if torf:
            c10.configure(text="◆")
            cc += 1
        elif not torf:
            c10.configure(text="◆", fg="gray")
    ccount.config(text=str(cc))

win = Tk()
win.title("돌깍기")


al = Label(win, text="증가능력", fg="blue")
al.grid(row=1, column=1)

total = Label(win, text="세공 성공 총 " + str(tot) + "회")
total.grid(row=1, column=3)

suc = Label(win, text="성공 확률 "+ str(percent) + "%")
suc.grid(row=1, column=4, columnspan=2)

aframe = LabelFrame(win, text="1번", fg="blue")
aframe.grid(row=2, column=3)
a1 = Label(aframe, text="◇", fg="blue")
a1.grid(row=1, column=1)
a2 = Label(aframe, text="◇", fg="blue")
a2.grid(row=1, column=2)
a3 = Label(aframe, text="◇", fg="blue")
a3.grid(row=1, column=3)
a4 = Label(aframe, text="◇", fg="blue")
a4.grid(row=1, column=4)
a5 = Label(aframe, text="◇", fg="blue")
a5.grid(row=1, column=5)
a6 = Label(aframe, text="◇", fg="blue")
a6.grid(row=1, column=6)
a7 = Label(aframe, text="◇", fg="blue")
a7.grid(row=1, column=7)
a8 = Label(aframe, text="◇", fg="blue")
a8.grid(row=1, column=8)
a9 = Label(aframe, text="◇", fg="blue")
a9.grid(row=1, column=9)
a10 = Label(aframe, text="◇", fg="blue")
a10.grid(row=1, column=10)
acount = Label(win, text=str(ac))
acount.grid(row=2, column=4)
a1bt = Button(win, text="세공", fg="blue", command=aclicked)
a1bt.grid(row=2, column=5)

bframe = LabelFrame(win, text="2번", fg="blue")
bframe.grid(row=3, column=3)
b1 = Label(bframe, text="◇", fg="blue")
b1.grid(row=1, column=1)
b2 = Label(bframe, text="◇", fg="blue")
b2.grid(row=1, column=2)
b3 = Label(bframe, text="◇", fg="blue")
b3.grid(row=1, column=3)
b4 = Label(bframe, text="◇", fg="blue")
b4.grid(row=1, column=4)
b5 = Label(bframe, text="◇", fg="blue")
b5.grid(row=1, column=5)
b6 = Label(bframe, text="◇", fg="blue")
b6.grid(row=1, column=6)
b7 = Label(bframe, text="◇", fg="blue")
b7.grid(row=1, column=7)
b8 = Label(bframe, text="◇", fg="blue")
b8.grid(row=1, column=8)
b9 = Label(bframe, text="◇", fg="blue")
b9.grid(row=1, column=9)
b10 = Label(bframe, text="◇", fg="blue")
b10.grid(row=1, column=10)
bcount = Label(win, text=str(bc))
bcount.grid(row=3, column=4)
bbt = Button(win, text="세공", fg="blue", command=bclicked)
bbt.grid(row=3, column=5)

cl = Label(win, text="감소능력", fg="red")
cl.grid(row=4, column=1)

fai = Label(win, text="균열 확률 "+ str(percent) + "%")
fai.grid(row=4, column=4, columnspan=2)

cframe = LabelFrame(win, text="2번", fg="red")
cframe.grid(row=5, column=3)
c1 = Label(cframe, text="◇", fg="red")
c1.grid(row=1, column=1)
c2 = Label(cframe, text="◇", fg="red")
c2.grid(row=1, column=2)
c3 = Label(cframe, text="◇", fg="red")
c3.grid(row=1, column=3)
c4 = Label(cframe, text="◇", fg="red")
c4.grid(row=1, column=4)
c5 = Label(cframe, text="◇", fg="red")
c5.grid(row=1, column=5)
c6 = Label(cframe, text="◇", fg="red")
c6.grid(row=1, column=6)
c7 = Label(cframe, text="◇", fg="red")
c7.grid(row=1, column=7)
c8 = Label(cframe, text="◇", fg="red")
c8.grid(row=1, column=8)
c9 = Label(cframe, text="◇", fg="red")
c9.grid(row=1, column=9)
c10 = Label(cframe, text="◇", fg="red")
c10.grid(row=1, column=10)
ccount = Label(win, text=str(cc))
ccount.grid(row=5, column=4)
cbt = Button(win, text="세공", fg="red", command=cclicked)
cbt.grid(row=5, column=5)

win.mainloop()
