p = [i for i in input()]
l = len(p)

def checklist(p, l):
    check = 0
    for _ in range(l):
        if p.pop() == '(':
            check += 1
        else:
            check -= 1

    if check:
        return False
    return True

# print(checklist(p, l))


def stackcheck(p, l):
    stack = [0]*l
    c = 0
    for i in range(l):
        if p[i] == '(':
            stack[c] = p[i]
            c += 1
        else:
            if stack[c-1] == '(':
                stack.pop(c-1)
                c -= 1
            else:
                stack[c] = p[i]
                c += 1
    return stack
            
print(stackcheck(p, l))