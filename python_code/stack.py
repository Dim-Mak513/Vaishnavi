def isempty(s):
    if len(s)==0:
        return True
    else:
        return False
    
def opush(s,element):
    s.append(element)

def top(s):
    if isempty(s):
        print("empty")
        return None
    else:
        print(s[-1])
    # x= len(s)
    # return s[x-1]

# show element of stack using for loop 
def pop(s):
    if isempty(s):
        print("underflow")
        return None
    else:
        print(s.pop())
    
def length(s):
    print(len(s))

def show(s):
    if isempty(s):
        print("underflow")
        return None
    else :
        for i in s:
            print(i)
    

'''stack=[] # list() use this instead
# stack=list()
a=isempty(stack)
print(a)

opush(stack,10)
opush(stack,20)
opush(stack,30)
opush(stack,40)

print(stack)

pop(stack)
top(stack)
length(stack)
show(stack)'''

print("initially the stack is empty")
print("enter 1 - push element","enter 2- pop","enter 3-show")
a=int(input("enter"))
if a==1:
    print("how many elements you want to push?")
    b=int(input("enter the no. of elements"))
    
        