import random
import sys
from typing import Any, Callable, List, Tuple

#length of progress bar
BAR_LENGTH = 25

class Predicate:
    """A predictae class.

    name:
        name of predicate
    first_q:
        first quantifier of predicate
    second_q:
        second quantifier of predicate
    """
    name: str
    first_q: bool
    second_q: bool

    def __init__(self, name: str, q1: bool, q2: bool):
        self.name = name
        self.first_q = q1
        self.second_q = q2
        

def func(compare_function: Callable, setA: List[int],
        setB: List[int], predicate: Predicate):
    """Function for comparing two sets with two quantifies.

       <compare_function> binary function to return bool
       <setA> <setB> are lists with items
       <allA> first quantifier
       <allB> second quantifier
       True for quantifier means Universal
       False for quantifier means Existential
    """
    allA = predicate.first_q
    allB = predicate.second_q
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
    
def implies(lis: List[Tuple[bool, bool]]):
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


#change random number to be rando anything
def check_predicate(pred1: Predicate, pred2: Predicate,
                   to_num1: int = 10, to_num2: int = 10, 
                   set_len1: int = 5, set_len2: int = 5):
    """Check all the predicates.
    """
    total_iter = to_num1 * to_num2
    counter = 0
    
    results = []
    for i in range(to_num1):
        for j in range(to_num2):
            progress_bar('check_predicates', total_iter, counter)

            for _ in range(100):
                S = [random.randint(0, i) for item in range(set_len1)]
                T = [random.randint(0, j) for item in range(set_len2)]

                pred1_res = func(greaterThan, S, T, pred1)
                pred2_res = func(greaterThan, S, T, pred2)

                results.append((pred1_res, pred2_res))

            counter += 1
    print()
    return results

def progress_bar(func_name: Callable, total: int, count: int):
    """Print a progress bar.
    """
    percent_done = round(100 * ((count + 1) / total), 1)

    finished = round(percent_done / (100 / BAR_LENGTH))
    not_finished = BAR_LENGTH - finished

    done = '█' * finished
    working = '░' * not_finished 
    print(f'Running \"{func_name}\": [{done}{working}] - {percent_done}% Finished', end='\r')

def get_all_pairs(lis: List[Predicate]):
    """Get all pairs of predicates.
    """
    ret = []
    for pred in lis:
        for pred2 in lis:
            ret.append((pred, pred2))
    return ret


#PREDICATES
G0 = Predicate('G0', True, True)
G1 = Predicate('G1', True, False)
G2 = Predicate('G2', False, True)
G3 = Predicate('G3', False, False)

#FUNCTION GIVEN
greaterThan = lambda a, b : a > b 

all_pairings = get_all_pairs([G0, G1, G2, G3])
for item in all_pairings:
    results = check_predicate(item[0], item[1], 5, 5)
    print(f'{item[0].name} implies {item[1].name}: {implies(results)}')
    print()