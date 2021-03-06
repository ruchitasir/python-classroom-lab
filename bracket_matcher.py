from collections import deque 

def bracket_matcher(input): 
    stack = deque() 
    opening= ['{','(','[']
    closing = ['}',')',']']

    for each in input:
        if each in opening:
            # print(each)
            stack.append(each)
        elif each in closing:
            if(len(stack)!=0):
                  index = closing.index(each)
                  ele = stack[len(stack)-1]
                  if(ele == opening[index]):
                      stack.pop()
            elif (len(stack)== 0):         
                       return False 
         
    #print('stack',stack)
    # for each in stack:
    #      print('stack finally',each)
    # print(len(stack))     
    if len(stack)== 0:
        return True
    return False            

status = bracket_matcher('{ac}}e{{hs}')
print('status',status)

status1 = bracket_matcher('a{()}}')
print('status',status1)


print('abc(123)',bracket_matcher('abc(123)'))
# returns true

print('a[b]c(123',bracket_matcher('a[b]c(123'))
# returns false -- missing closing parens

print('a[bc(123)]',bracket_matcher('a[bc(123)]'))
# returns true

print('a[bc(12]3)',bracket_matcher('a[bc(12]3)'))
# returns false -- improperly nested

print('a{b}{c(1[2]3)}',bracket_matcher('a{b}{c(1[2]3)}'))
# returns true

print('a{b}{c(1}[2]3)',bracket_matcher('a{b}{c(1}[2]3)'))
# returns false -- improperly nested

print('()',bracket_matcher('()'))
# returns true

print('[]]',bracket_matcher('[]]'))
# returns false - no opening bracket to correspond with last character

print('abc123yay',bracket_matcher('abc123yay'))
# returns true -- no brackets = correctly matched