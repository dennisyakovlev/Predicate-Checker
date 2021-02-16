def func(compare_function, setA, setB, allA = True, allB = True):
    funcFirst = (lambda a, b : a and b) if allA else (lambda a, b : a or b)
    funcSecond = (lambda a, b : a and b) if allB else (lambda a, b : a or b)

    truth = compare_function(setA[0], setB[0])
    lisBig = []
    for A in setA:
        lis = []
        for B in setB:
            lis.append(compare_function(A, B))

        truth = funcSecond(lis[0], lis[1])
        for item in lis[1:]:
            truth = funcSecond(truth, item)

    truth = funcFirst(lisBig[0], lisBig[1])
    for item in lisBig[1:]:
        truth = funcFirst(truth, item)
    print(truth)
    

lessThan = lambda a, b : a > b  

setA = [1,2,5]
setB = [3,4,1]

func(lessThan, setA, setB, False, True)