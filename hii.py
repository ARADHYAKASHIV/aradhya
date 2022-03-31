def isempty(Arr):
    if len(Arr)==0:
        return True
    else:
        return False

def push(Arr,item):
    Arr.append(item)
    top=len(Arr)-1

def show(Arr):
    if isempty(Arr):
        print('EMPTY STACK')
    else:
        t= len(Arr)-1
        print("(top)",end='')
        while (t>=0):
            print(Arr[t], '<==', end='')
            t=t-1
            print()




def POP(Arr):
    if isempty(Arr):
        return 'underfolw occurs'
    else:
        val=Arr.pop()
        if len(Arr)==0:
            top=None
        else:
            top=len(Arr)-1
            return val

Arr=[]
top=None
while True:
    print("**********STACK IMPIMENTATION BY LIST**********")
    print('1:push')
    print('2:pop')
    print('3:show')
    print('0:exit')
    ch=int(input('enter your choice:- '))
    if ch==1:
        val=int(input('Enter no. to push'))
        push(Arr,val)
    elif ch==2:
        val=POP(Arr)
        if val=='underflow':
            print('empty stack')
        else:
            print('\nDeleted item: ',val) 

    elif ch==3:
        show(Arr)
    elif ch==0:
        print('bey bye') 
        break