import random

def func(compare_function, setA, setB, allA = True, allB = True):
    """Function for comparing two sets with two quantifies.

       <compare_function> binary function to return bool
       <setA> <setB> are lists with items
       <allA> first quantifier
       <allB> second quantifier
       True for quantifier means Universal
       False for quantifier means Existential
    """
    #Existential quantifier can be rewritten as OR statement
    #Universal quantifier can be rewritten as AND statement
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
        lisBig.append(truth)

    truth = funcFirst(lisBig[0], lisBig[1])
    for item in lisBig[1:]:
        truth = funcFirst(truth, item)
   
    return truth
    
G0 = (True, True)
G1 = (True, False)
G2 = (False, True)
G3 = (False, False)

#lis = random.sample(range(0, 10), 5)
#print(lis)


lessThan = lambda a, b : a > b  

setA = [1,2,5]
setB = [3,5,1]

print(func(lessThan, setA, setB, False, True))