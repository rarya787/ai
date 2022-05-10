'''
Aim:
Implementation of Constraint Satisfactory problem- CryptArithmatic Problem (‘SEND +
MORE = MONEY’)
Problem Statement:
Given an expression where two words add to give a third word, assign some unique digit (0-
9) to each letter where same letters cannot be assigned to different digit. The objective is to
find out the digit represented by each letter that satisfies a given equation.

SEND
+ MORE
= MONEY
In this example, the solution to the puzzle is:
O = 0, M = 1, Y = 2, E = 5, N = 6, D = 7, R = 8, and S = 9.
which gives us:

9567
+ 1085
= 10652
Algorithm:
1. Start.
2. Accept a expression. “SEND +MORE = MONEY”.
3. Extract the words SEND, MORE and MONEY.
4. Permute for different combination of values for S,E,N,D,M,O,R,Y.
5. Check if the sum of the left value i.e, SEND + MORE is equal to the right sum i.e,
MONEY or NOT. If the sum value matches, print the mapping.
6. Continue for other permutation as well.
7. Stop.
'''
import itertools
def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s
def solve2(equation):
    left, right = equation.lower().replace(' ', '').split('=')
    left = left.split('+')
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            print(' + '.join(str(get_value(word, sol)) for word in left) + " = {} (mapping: {})".format(get_value(right, sol), sol))
            
if __name__ == '__main__':
  eq = input("Enter an equation: ")
  solve(eq)
