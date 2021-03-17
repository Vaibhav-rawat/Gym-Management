'''This program was written to keep the record for three people which are supposed to be the existing member 
of the gym and this program updates and maintain the log files(Exercise and Diet) of the corresponding members
Author - Vaibhav Rawat
Purpose - Python problem solving'''
def getdata():
    import datetime
    return datetime.datetime.now()

def log():
    person=int(input('1 for Harry\n2 for Rohan\n3 for Hammad\n'))
    if person==1:
        p=int(input('1 for diet\n2 for exercise\n'))
        if p==1:
            with open('harry.txt','a') as h:
                content=input('Please write\n')
                h.writelines(f'{getdata()}-->{content}\n')
                print('noted\n')
        elif p==2:
            with open('harry_exercise.txt','a') as h:
                content=input('Please write\n')
                h.writelines(f'{getdata()}-->{content}\n')
                print('noted\n')
    elif person==2:
        q=int(input('1 for diet\n2 for exercise\n'))
        if q==1:
            with open('Rohan.txt','a') as r:
                content=input('Please write\n')
                h.writelines(f'{getdata()}-->{content}\n')
                print('noted\n')
        elif q==2:
            with open('Rohan_exercise.txt','a') as r:
                content=input('Please write\n')
                r.writelines(f'{getdata()}-->{content}\n')
                print('noted\n')
    elif person==3:
        r=int(input('1 for diet\n2 for exercise\n'))
        if r==1:
            with open('Hammad.txt','a') as h:
                content=input('Please write\n')
                h.writelines(f'{getdata()}-->{content}\n')
                print('noted\n')
        elif r==2:
            with open('Hammad_exercise.txt','a') as h:
                content=input('Please write\n')
                h.writelines(f'{getdata()}-->{content}\n')
                print('noted\n')
    else:
        print('wrong input\n')

def retrieve():
    person=int(input('1 for Harry\n2 for Rohan\n3 for Hammad\n'))
    if person==1:
        x=int(input('1 for diet\n2 for exercise\n'))
        if x==1:
            with open('harry.txt','r') as h:
                print(h.read())
        elif x==2:
            with open('harry_exercise.txt','r') as h:
                print(h.read())
    elif person==2:
        y=int(input('1 for diet\n2 for exercise\n'))
        if y==1:
            with open('Rohan.txt','r') as m:
                print(m.read())
        elif y==2:
            with open('Rohan_exercise.txt','r') as h:
                print(m.read())
    elif person==3:
        z=int(input('1 for diet\n2 for exercise\n'))
        if z==1:
            with open('Hammad.txt','r') as t:
                print(t.read())
        elif z==2:
            with open('Hammad_exercise.txt','r') as h:
                print(t.read())
    else:
        print('wrong input\n')

print('Hello Vaibhav how are you?')
n=int(input('Press 1 for Log\nPress 2 for Retrieve\n'))

if n==1:
    log()
elif n==2:
    retrieve()
