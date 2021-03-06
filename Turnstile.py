from collections import deque
def turnstile(numCustomers, arrTime, direction):
    inque = deque([])
    outque = deque([])
    piv = 0
    rtn = [-1]* numCustomers
    isOut = False
    cost = 0
    while inque or outque or piv < numCustomers:
        print(inque, outque, piv, isOut)
        while piv < numCustomers and arrTime[piv] == cost:
            if direction[piv] == 1:
                outque.append(piv)
                if cost == 0:
                    isOut = True
            else:
                inque.append(piv)
            piv += 1
        if (isOut and outque )or (not inque and not isOut and outque):
            popindex = outque.popleft()
            rtn[popindex] = cost
            cost+=1
            isOut = True
        elif inque:
            popindex = inque.popleft()
            rtn[popindex] = cost
            cost+=1
            isOut = False
        else:
            isOut = True
            cost+=1
        print(rtn)
    return rtn


    
    
    
numCustomers = 5
arrTime =   [0,0,1,100, 100]
direction = [0,1,1,0,1]
print(turnstile(numCustomers, arrTime,direction))