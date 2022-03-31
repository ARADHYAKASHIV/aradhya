def isempty(Arr):
    if len(Arr)==0:
        return True
    else:
        return False

def push(Arr,item):
    if item %5==0:
        Arr.append(item)
        top= len(Arr)-1
    else:
        print('\n$$$$   INVALID STACK   $$$$\n')

def show(Arr):
    if isempty(Arr):
        print('no item found')
    else:
        t= len(Arr)-1
        print('(TOP)',end="")
        while (t>=0):
            print(Arr[t],'<==',end="")
            t=t-1
        

Arr=[]
top= None
while True:
    print('**********STACK IMPLEMENTATION BY LIST**********')
    print('1:push')
    print('2:show')
    print('0:exit')
    ch= int(input('Enter You Choice:-'))
    if ch==1:
        val=int(input('Enter Value To Push:-'))
        push(Arr,val)
    elif ch==2:
        show(Arr)
    elif ch==0:
        print('bye bye')
        break