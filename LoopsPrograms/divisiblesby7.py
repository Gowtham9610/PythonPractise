div = 7

def divs(start, stop, value):
    result = []
    for i in range(start,stop):
        if i%value == 0 :
            result.append(str(i))
    return (','.join(result))

print(divs(1500,2501,7))
