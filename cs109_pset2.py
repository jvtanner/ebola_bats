# Do NOT add any other import statements
import numpy as np

# Name: Joshua Tanner

"""
Starter Code for CS 109 Problem Set 2, Question 14

************************IMPORTANT************************
For part_a and part_b, do NOT modify the name of the 
functions. Do not add or remove parameters to them either.
Moreover, make sure your return value is exactly as 
described in the PDF handout and in the provided function 
comments. Remember that your code is being autograded. You
are free to write helper functions if you so desire.
Do NOT rename this file.
************************IMPORTANT************************
"""

def part_a(filename="bats.csv"):
    """
    filename is a path to a csv file, e.g. "bats.csv".
    You must use the filename variable. Do NOT alter the 
    filename variable, and do NOT hard-code a filepath;
    if you do, you'll likely fail the autograder.

    You should return a numpy array of length 6, 
    call it probs. probs[i] should be P(G_i) for 
    0 <= i <= 4. probs[5] should be P(T).

    See the assignment handout for some advice on how 
    to use numpy to make your life easier in this 
    function.
    """
    data = np.genfromtxt(filename, delimiter=',')
    return np.mean(data, axis=0)


def part_b(filename="bats.csv"):
    """
    filename is a path to a csv file, e.g. "bats.csv".
    As in part_a, you must use this variable or you'll
    likely fail the autograder.

    You should return a numpy array of length 5, call it 
    probs, where probs[i] is equal to P(T | G_i). See 
    the assignment handout for some information on 
    numpy functionality that'll help you here.
    """
    data = np.genfromtxt(filename, delimiter=',')
    g0 = data[np.where(data[:, 0] == 1)]
    g1 = data[np.where(data[:, 1] == 1)]
    g2 = data[np.where(data[:, 2] == 1)]
    g3 = data[np.where(data[:, 3] == 1)]
    g4 = data[np.where(data[:, 4] == 1)]

    t_g0 = len(g0[np.where(g0[:, 5] == 1)]) / len(g0)
    t_g1 = len(g1[np.where(g1[:, 5] == 1)]) / len(g1)
    t_g2 = len(g2[np.where(g2[:, 5] == 1)]) / len(g2)
    t_g3 = len(g3[np.where(g3[:, 5] == 1)]) / len(g3)
    t_g4 = len(g4[np.where(g4[:, 5] == 1)]) / len(g4)
    probs = np.array([t_g0, t_g1, t_g2, t_g3, t_g4])
    return probs


def part_c():
    """
    We won't autograde anything you write in this function.
    You should submit your answer to part (c) in the PDF
    you upload to Gradescope. But we've included this function
    here for convenience. It will get called by our provided
    main method. Feel free to do whatever you want here, 
    including leaving this function blank. We won't read it.
    """
    pass


def main():
    """
    We've provided this for convenience, simply to call the 
    functions above for parts a, b, and c. Feel free to modify
    this function however you like. We won't grade anything
    in this function.
    """
    print("*** Beginning part (a) on 'bats.csv' ***")
    probs = part_a()
    print(f"part (a) returned {probs}")
    print("*** Ending part (a) ***\n")

    print("*** Beginning part (b) on 'bats.csv' ***")
    cond_probs = part_b()
    print(f"part (b) returned {cond_probs}")
    print("*** Ending part (b) ***\n")

    print("*** Beginning part (c) - convenience function ***")
    part_c()
    print("*** Ending part (c) ***")


# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()
