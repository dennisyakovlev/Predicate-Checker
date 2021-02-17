import random
import sys

#PREDICATES
G0 = (True, True)
G1 = (True, False)
G2 = (False, True)
G3 = (False, False)

#FUNCTION
greaterThan = lambda a, b : a > b  

def func(compare_function, setA, setB, predicate):
    """Function for comparing two sets with two quantifies.

       <compare_function> binary function to return bool
       <setA> <setB> are lists with items
       <allA> first quantifier
       <allB> second quantifier
       True for quantifier means Universal
       False for quantifier means Existential
    """
    allA = predicate[0]
    allB = predicate[1]
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
    
def implies(lis):
    """Check if when first bool of tuple 
       is true then second one is too.
    """
    hasOneTrue = False
    for item in lis:
        if item[0]:
            hasOneTrue = True
            if not item[1]:
                return False
    if not hasOneTrue:
        print("first bool is always false.")
    return True

def check_predicates(toNum1 = 10, toNum2 = 10):
    total_iter = toNum1 * toNum2
    counter = 0
    
    results = []
    for i in range(toNum1):
        for j in range(toNum2):
            #sys.stdout.write(f"\r#" * counter)
            #sys.stdout.flush()
            for _ in range(100):
                S = [random.randint(0, i) for item in range(5)]
                T = [random.randint(0, j) for item in range(5)]

                pred1 = func(greaterThan, S, T, G2)
                pred2 = func(greaterThan, S, T, G0)

                results.append((pred1, pred2))



print(implies(results))