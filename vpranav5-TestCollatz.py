#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)


    def test_read2(self):
        s = "-5 5\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  -5)
        self.assertEqual(j, 5)

    def test_read3(self):
        s = "30 15\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  30)
        self.assertEqual(j, 15)

    def test_read4(self):
        s = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 1)
        

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)


    def test_eval_5(self):
        v = collatz_eval(500, 20) # Corner Case 1
        self.assertEqual(v, 144)

    def test_eval_6(self):
        v = collatz_eval(1, 1) # Corner Case 2
        self.assertEqual(v, 1)

    def test_eval_7(self):
        v = collatz_eval(55, 5555) 
        self.assertEqual(v, 238)

    # test if the exact interval in cache exists
    def test_eval_8(self):
        v = collatz_eval(501, 1000) 
        self.assertEqual(v, 179)

    # test if the prev and next intervals are in cache
    def test_eval_9(self):
        v = collatz_eval(538, 3332) 
        self.assertEqual(v, 217)
    
    # test if the prev and next intervals are in cache
    def test_eval_10(self):
        v = collatz_eval(510, 1520) 
        self.assertEqual(v, 182)

    def test_eval_11(self):
        v = collatz_eval(300, 1005) 
        self.assertEqual(v, 179)

    def test_eval_12(self):
        v = collatz_eval(20, 50) 
        self.assertEqual(v, 112)

    # test if middle interval cannot be looked up
    def test_eval_13(self):
        v = collatz_eval(500, 1003) 
        self.assertEqual(v, 179)

    # test case when only the last interval can be looked up
    def test_eval_14(self):
        v = collatz_eval(238, 541) 
        self.assertEqual(v, 144)

    # test case when first interval can't be looked up
    def test_eval_15(self):
        v = collatz_eval(538, 2000) 
        self.assertEqual(v, 182)

    # test case when last interval needs to be computed
    def test_eval_16(self):
        v = collatz_eval(500, 1020) 
        self.assertEqual(v, 179)
    
     # test case when first and second interval can't be looked up
    def test_eval_17(self):
        v = collatz_eval(1234, 3003) 
        self.assertEqual(v, 217)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print2(self):
        w = StringIO()
        collatz_print(w, 500, 20, 144)
        self.assertEqual(w.getvalue(), "500 20 144\n")


    def test_print3(self):
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_print4(self):
        w = StringIO()
        collatz_print(w, 55, 5555, 238)
        self.assertEqual(w.getvalue(), "55 5555 238\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # handle 12 new test cases for collatz_solve()
    def test_solve2(self):
        r = StringIO("20 60\n85 944\n678 55\n10 10\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "20 60 113\n85 944 179\n678 55 145\n10 10 7\n")


    def test_solve3(self):
        r = StringIO("50 30\n45 434\n2 5\n9000 10000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "50 30 110\n45 434 144\n2 5 8\n9000 10000 260\n")


    def test_solve4(self):
        r = StringIO("1000 2\n800 5600\n87 45\n15 10\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1000 2 179\n800 5600 238\n87 45 116\n15 10 18\n")


# ----
# main
# ----

if __name__ == "__main__": #pragma: no cover
    main()

""" #pragma: no cover
% coverage run --branch TestCollatz.py >  TestCollatz.out 2>&1


% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


% coverage report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
