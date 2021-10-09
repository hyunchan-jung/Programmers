def solution(s):
    stack = []
    for i in s:
        print(i, stack)
        if i == '(':
            stack.append(i)
        elif len(stack) == 0 or stack.pop() == None:
            return False
    
    if len(stack) == 0:
        return True
    else:
        return False